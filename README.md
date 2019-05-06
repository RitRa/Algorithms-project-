# Benchmarking Sorting Algorithms Project
Semester 3, GMIT, 2019

Sorting is organising data in ascending or descending order. This project will take a comparative look at 6 sorting algorithms (Bubble Sort, Merge Sort, Counting Sort, Quick Sort, Insertion Sort, BogoSort). It is in two parts, firstly an overview of each algorithm and lastly the benchmarking application of the sorting algorithms.

### Sorting Algorithms Overview:
1. How it works 
2. Performance or Time complexity. Time Complexity is the computational complexity that describes the amount of time it takes to run an algorithm. (source: https://en.wikipedia.org/wiki/Time_complexity)
3. An example diagram of how it works
4. A python example of the selected algorithm (with comments) 

This project will also highlight the different sorting methods used in each algorithm whether the are comparison based or non-comparison based. 

### The Benchmarking Application

Using python(https://www.python.org/), random number arrays were created ranging in sizes from 100 to 50,000. The sorting algorithms will each run through the arrays and the timings will be captured using Python’s time module (https://docs.python.org/3/library/time.html). These timings are collected into a table, using the library pandas tables https://pandas.pydata.org/. The timings will be benchmarked against one another in a plot using Seaborn https://seaborn.pydata.org/ and Matplotlib https://matplotlib.org/. 

The result of the benchmarking sorting algorithm application are discussed to see if they matched the expected output. 
 
This project is written using a Jupyter notebook (https://jupyter.org/) using external python files.
