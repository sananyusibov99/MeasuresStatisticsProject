from tkinter import *
from functools import partial
import statistics
from tkinter import messagebox

root = Tk()
root.title("Measures in Statistics")
root.resizable(False, False)
data = StringVar()

variance = 0
standardDeviation = 0


def calculateFunctions(data):
    calculateMean(data)
    calculateMedian(data)
    calculateMode(data)
    calculateIQR(data)
    calculateMin(data)
    calculateMax(data)
    calculateCountN(data)
    calculateVariance(data)
    calculateStandardDeviation(data)


def calculateMean(data):
    global mean, sum
    sum = 0
    count = 0
    for item in data:
        sum += int(item)
        count += 1
    mean = sum / count


def calculateMedian(data):
    global median
    ints = [int(item) for item in data]
    ints.sort()
    mid = len(ints) // 2
    median = (int(ints[mid]) + int(ints[~mid])) / 2.0


def calculateMode(data):
    global mode
    ints = [int(item) for item in data]
    modeList = statistics.multimode(ints)
    mode = ""
    for item in modeList:
        mode += str(item) + ", "
    mode = mode[:-2]


def calculateIQR(data):
    global IQR
    ints = [int(item) for item in data]
    ints.sort()
    if len(ints) % 2 == 0:
        intsQ1 = []
        intsQ3 = []
        for i in range(len(ints) // 2):
            intsQ1.append(ints[i])
        for i in range(len(ints) // 2, len(ints)):
            intsQ3.append(ints[i])

        midQ1 = len(intsQ1) // 2
        medianQ1 = (int(intsQ1[midQ1]) + int(intsQ1[~midQ1])) / 2.0
        midQ3 = len(intsQ3) // 2
        medianQ3 = (int(intsQ3[midQ3]) + int(intsQ3[~midQ3])) / 2.0
        IQR = medianQ3 - medianQ1
    elif len(ints) % 2 != 0:
        intsQ1 = []
        intsQ3 = []
        for i in range(len(ints) // 2):
            intsQ1.append(ints[i])
        for i in range((len(ints) // 2) + 1, len(ints)):
            intsQ3.append(ints[i])

        midQ1 = len(intsQ1) // 2
        medianQ1 = (int(intsQ1[midQ1]) + int(intsQ1[~midQ1])) / 2.0
        midQ3 = len(intsQ3) // 2
        medianQ3 = (int(intsQ3[midQ3]) + int(intsQ3[~midQ3])) / 2.0
        IQR = medianQ3 - medianQ1


def calculateMin(data):
    global min
    ints = [int(item) for item in data]
    ints.sort()
    min = ints[:1]
    min = min[0]


def calculateMax(data):
    global max
    ints = [int(item) for item in data]
    ints.sort(reverse=True)
    max = ints[:1]
    max = max[0]


def calculateCountN(data):
    global countNumbers
    countNumbers = len(data)


def calculateVariance(data):
    global variance
    ints = [int(item) for item in data]
    if str(var.get()) == "1":
        print("Population")
        variance = statistics.pvariance(ints)
    elif str(var.get()) == "2":
        print("Sample")
        variance = statistics.variance(ints)


def calculateStandardDeviation(data):
    global standardDeviation
    ints = [int(item) for item in data]
    if str(var.get()) == "1":
        print("Population")
        standardDeviation = statistics.pstdev(ints)
    elif str(var.get()) == "2":
        print("Sample")
        standardDeviation = statistics.stdev(ints)


def Creator():
    messagebox.showinfo("Creator", "This application was made by Sanan Yusibov")


def reset():
    entryData.delete(0, END)
    labelMean.config(text="0")
    labelMedian.config(text="0")
    labelMode.config(text="0")
    labelIQR.config(text="0")
    labelMin.config(text="0")
    labelMax.config(text="0")
    labelCount.config(text="0")
    labelSum.config(text="0")
    labelVariance.config(text="0")
    labelStandardDev.config(text="0")


def submit(dat):
    global mean, median, mode, IQR, countNumbers, sum, variance, standardDeviation
    data = dat.get()
    data = data.replace(" ", "")
    data = data.split(",")
    try:
        calculateFunctions(data)
    except:
        messagebox.showerror("Bad input", "Please enter data separated by ,")

    mean = format(mean, '.5f')
    variance = format(variance, '.5f')
    standardDeviation = format(standardDeviation, '.5f')

    labelMean.config(text=mean)
    labelMedian.config(text=median)
    labelMode.config(text=mode)
    labelIQR.config(text=IQR)
    labelMin.config(text=min)
    labelMax.config(text=max)
    labelCount.config(text=countNumbers)
    labelSum.config(text=sum)
    labelVariance.config(text=variance)
    labelStandardDev.config(text=standardDeviation)


var = IntVar()
R1 = Radiobutton(root, text="Population", variable=var, value=1)
R1.grid(row=0, column=0, columnspan=2)

R2 = Radiobutton(root, text="Sample", variable=var, value=2)
R2.grid(row=0, column=2, columnspan=2)

labelData = Label(text="Enter data:").grid(row=1, column=0)
entryData = Entry(width=30, textvariable=data)
entryData.grid(row=1, column=1, columnspan=3)

Label(text="Mean:").grid(row=2, column=0)
labelMean = Label(text="0")
labelMean.grid(row=2, column=1)

Label(text="Median:").grid(row=3, column=0)
labelMedian = Label(text="0")
labelMedian.grid(row=3, column=1)

Label(text="Mode:").grid(row=4, column=0)
labelMode = Label(text="0")
labelMode.grid(row=4, column=1)

Label(text="Interquartile Range:").grid(row=5, column=0)
labelIQR = Label(text="0")
labelIQR.grid(row=5, column=1)

Label(text="Minimum:").grid(row=6, column=0)
labelMin = Label(text="0")
labelMin.grid(row=6, column=1)

Label(text="Maximum:").grid(row=7, column=0)
labelMax = Label(text="0")
labelMax.grid(row=7, column=1)

Label(text="Count N:").grid(row=8, column=0)
labelCount = Label(text="0")
labelCount.grid(row=8, column=1)

Label(text="Sum:").grid(row=9, column=0)
labelSum = Label(text="0")
labelSum.grid(row=9, column=1)

Label(text="Variance:").grid(row=10, column=0)
labelVariance = Label(text="0")
labelVariance.grid(row=10, column=1)

Label(text="Standard Deviation:").grid(row=11, column=0)
labelStandardDev = Label(text="0")
labelStandardDev.grid(row=11, column=1)

submit = partial(submit, data)
Button(text="Creator", command=Creator).grid(row=12, column=0)
Button(text="Submit", command=submit).grid(row=12, column=2)
Button(text="Reset", command=reset).grid(row=12, column=3)

root.mainloop()
