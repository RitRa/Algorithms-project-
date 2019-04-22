# importing the random numbers
from randomnumber import *

# algorithm
def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

# import time module
import time

#### benchmarking
num_runs = 10
results = []
insertsort_avglist = []


def benchmark_insertionsort():
    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call insertion sort
        insertionSort(alist)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    insertsort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call insertion sort
        insertionSort(alist1)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    insertsort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call insertion sort
        insertionSort(alist2)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    insertsort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call insertion sort
        insertionSort(alist3)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    insertsort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call insertion sort
        insertionSort(alist4)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    insertsort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call insertion sort
        insertionSort(alist5)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    insertsort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call insertion sort
        insertionSort(alist6)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    insertsort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call insertion sort
        insertionSort(alist7)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    insertsort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call insertion sort
        insertionSort(alist8)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    insertsort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call insertion sort
        insertionSort(alist9)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    insertsort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call insertion sort
        insertionSort(alist10)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    insertsort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call insertion sort
        insertionSort(alist11)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    insertsort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call insertion sort
        insertionSort(alist12)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    insertsort_avglist.append(average)

    print(insertsort_avglist)

benchmark_insertionsort()