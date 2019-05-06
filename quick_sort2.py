# importing the random numbers
from randomnumber import *

# Quick Sort
def printalistay(alist):
  return (' '.join(str(i) for i in alist))
 
def quicksort(alist, i, j):
  if i < j:
    pos = partition(alist, i, j)
    quicksort(alist, i, pos - 1)
    quicksort(alist, pos + 1, j)
 
def partition(alist, i, j):
  #pivot = alist[j] # pivot on the last item
  pivot = alist[int(j/2)] # pivot on the median
  small = i - 1
  for k in range(i, j):
    if alist[k] <= pivot:
      small += 1
      swap(alist, k, small)
 
  swap(alist, j, small + 1)
  print ("Pivot = " + str(alist[small + 1]), " alist = " + printalistay(alist))
  return small + 1
 
def swap(alist, i, j):
  alist[i], alist[j] = alist[j], alist[i]
 
#if __name__ == '__main__':
#    alist = [9, 4, 8, 3, 1, 2, 5]
#    print (" Initial alistay :",printalistay(alist))
#    quicksort(alist, 0, len(alist) - 1)


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
        quicksort(alist, 0, len(alist) - 1)
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
        quicksort(alist1, 0, len(alist) - 1)
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
        quicksort(alist2, 0, len(alist) - 1)
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
        quicksort(alist3, 0, len(alist) - 1)
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
        quicksort(alist4, 0, len(alist) - 1)
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
        quicksort(alist5, 0, len(alist) - 1)
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
        quicksort(alist6, 0, len(alist) - 1)
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
        quicksort(alist7, 0, len(alist) - 1)
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
        quicksort(alist8, 0, len(alist) - 1)
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
        quicksort(alist9, 0, len(alist) - 1)
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
        quicksort(alist10, 0, len(alist) - 1)
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
        quicksort(alist11, 0, len(alist) - 1)
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
        quicksort(alist12, 0, len(alist) - 1)
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
        quicksort(alist13, 0, len(alist) - 1)
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