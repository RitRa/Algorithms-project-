# importing the random numbers
from randomnumber import *

# Python program for implementation of Bogo Sort 
import random 
# Sorts array a[0..n-1] using Bogo sort 
def bogoSort(alist): 
    n = len(alist) 
    while (is_sorted(alist)== False): 
        shuffle(alist) 
  
# To check if array is sorted or not 
def is_sorted(alist): 
    n = len(alist) 
    for i in range(0, n-1): 
        if (alist[i] > alist[i+1] ): 
            return False
    return True
  
# To generate permuatation of the array 
def shuffle(alist): 
    n = len(alist) 
    for i in range (0,n): 
        r = random.randint(0,n-1) 
        alist[i], alist[r] = alist[r], alist[i]


#### benchmarking
# import time module
import time
num_runs = 10
results = []
bogosort_avg = []

def benchmark_bogort():
    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call insertion sort
        bogoSort(alist)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    bogosort_avg.append(average)
    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call insertion sort
        bogoSort(alist1)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    bogosort_avg.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call insertion sort
        bogoSort(alist2)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    bogosort_avg.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call insertion sort
        bogoSort(alist3)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    bogosort_avg.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call insertion sort
        bogoSort(alist4)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    bogosort_avg.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call insertion sort
        bogoSort(alist5)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    bogosort_avg.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call insertion sort
        bogoSort(alist6)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    bogosort_avg.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call insertion sort
        bogoSort(alist7)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    bogosort_avg.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call insertion sort
        bogoSort(alist8)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    bogosort_avg.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call insertion sort
        bogoSort(alist9)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    bogosort_avg.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call insertion sort
        bogoSort(alist10)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    bogosort_avg.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call insertion sort
        bogoSort(alist11)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    bogosort_avg.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call insertion sort
        bogoSort(alist12)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    bogosort_avg.append(average)

    print(bogosort_avg)

benchmark_bogort()