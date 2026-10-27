# Measures in Statistics

A small desktop app that calculates the main numerical measures for a data set. I made it for the mathematics exam on numerical measures in statistics, part of the Data Science master's programme at UFAZ (December 2020).

## What it calculates

Enter numbers separated by commas, choose **Population** or **Sample**, and click Submit. The app shows:

- mean, median and mode (all modes, if there are several)
- interquartile range (IQR), found from the medians of the lower and upper halves
- minimum, maximum, count and sum
- variance and standard deviation, using the population or sample formula

Reset clears the input. If the input is invalid, an error message is shown.

## Tech stack

Python 3.8+, Tkinter, `statistics` module

## How to run

```bash
python main.py
```

No extra packages are needed: Tkinter comes with Python.
