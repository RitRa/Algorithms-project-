# importing the random numbers
from randomnumber import *

# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheQuickSort.html

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

# import time module
import time

num_runs = 10
results = []
quicksort_avglist = []

def benchmark_quick():
    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call quick sort
        quickSort(alist)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    average = round(average, 3)
    quicksort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call quick sort
        quickSort(alist1)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    average = round(average, 3)
    quicksort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call quick sort
        quickSort(alist2)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    average = round(average, 3)
    quicksort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call quick sort
        quickSort(alist3)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    average = round(average, 3)
    quicksort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call quick sort
        quickSort(alist4)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    average = round(average, 3)
    quicksort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call quick sort
        quickSort(alist5)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    average = round(average, 3)
    quicksort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call quick sort
        quickSort(alist6)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    average = round(average, 3)
    quicksort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call quick sort
        quickSort(alist7)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    average = round(average, 3)
    quicksort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call quick sort
        quickSort(alist8)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    average = round(average, 3)
    quicksort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call quick sort
        quickSort(alist9)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    average = round(average, 3)
    quicksort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call quick sort
        quickSort(alist10)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    average = round(average, 3)
    quicksort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call quick sort
        quickSort(alist11)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    average = round(average, 3)
    quicksort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call quick sort
        quickSort(alist12)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    # round to 3 decimals
    average = round(average, 3)
    quicksort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call quick sort
        quickSort(alist13)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    # round to 3 decimals
    average = round(average, 3)
    quicksort_avglist.append(average)
    
    
    print(quicksort_avglist)

benchmark_quick()