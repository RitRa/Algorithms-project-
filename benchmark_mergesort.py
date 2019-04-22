# importing the random numbers
from randomnumber import *

# code sourced from http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html

def mergeSort(alist):
    #print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1




# import time module
import time

num_runs = 10
results = []
mergesort_avglist = []


def benchmark_merge():
    

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## mergeSort
        mergeSort(alist)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    mergesort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## mergeSort
        mergeSort(alist1)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    mergesort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## mergeSort
        mergeSort(alist2)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    mergesort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## mergeSort
        mergeSort(alist3)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    mergesort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## mergeSort
        mergeSort(alist4)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    mergesort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## mergeSort
        mergeSort(alist5)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    mergesort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## mergeSort
        mergeSort(alist6)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    mergesort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## mergeSort
        mergeSort(alist7)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    mergesort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## mergeSort
        mergeSort(alist8)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    mergesort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## mergeSort
        mergeSort(alist9)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    mergesort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## mergeSort
        mergeSort(alist10)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    mergesort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## mergeSort
        mergeSort(alist11)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    mergesort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## mergeSort
        mergeSort(alist12)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    mergesort_avglist.append(average)

    return mergesort_avglist

benchmark_merge()