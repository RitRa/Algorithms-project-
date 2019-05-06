# testing algorithm from notes
# importing the random numbers
from randomnumber import *

  
def insertionSort(alist):
  N = len(alist)
  for i in range(1, N):
    j = i - 1
    temp = alist[i]
    while j >= 0 and temp < alist[j]:
      alist[j + 1] = alist[j]
      j -= 1
    alist[j + 1] = temp
    #print ("After pass " + str(i) + "  :", alist)
    
    
   

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
    # round to 3 decimals
    average = round(average, 3)
    #add to alistay
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
    # round to 3 decimals
    average = round(average, 3)
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
    # round to 3 decimals
    average = round(average, 3)
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
    # round to 3 decimals
    average = round(average, 3)
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
    # round to 3 decimals
    average = round(average, 3)
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
    # round to 3 decimals
    average = round(average, 3)
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
    # round to 3 decimals
    average = round(average, 3)
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
    # round to 3 decimals
    average = round(average, 3)
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
    # round to 3 decimals
    average = round(average, 3)
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
    # round to 3 decimals
    average = round(average, 3)
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
    # round to 3 decimals
    average = round(average, 3)
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
    # round to 3 decimals
    average = round(average, 3)
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
    # round to 3 decimals
    average = round(average, 3)
    insertsort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## call insertion sort
        insertionSort(alist13)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
        
    b = sum(results)
    average = (b/num_runs)
    # round to 3 decimals
    average = round(average, 3)
    insertsort_avglist.append(average)
    
    print(insertsort_avglist)

benchmark_insertionsort()