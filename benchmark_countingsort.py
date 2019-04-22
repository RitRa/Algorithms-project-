# importing the random numbers
from randomnumber import *

# code sourced http://www.learntosolveit.com/python/algorithm_countingsort.html
def counting_sort(array, maxval):
    """in-place counting sort"""
    n = len(array)
    m = maxval + 1
    count = [0] * m               # init with zeros
    for a in array:
        count[a] += 1             # count occurences
    i = 0
    for a in range(m):            # emit
        for c in range(count[a]): # - emit 'count[a]' copies of 'a'
            array[i] = a
            i += 1
    return array


# import time module
import time

num_runs = 10
results = []
countsort_avglist = []

def benchmark_countingsort():
    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## counting sort
        counting_sort(alist, 100)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    countsort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## counting sort
        counting_sort(alist1, 250)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    countsort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## counting sort
        counting_sort(alist2, 500)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    countsort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## counting sort
        counting_sort(alist3, 750)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    countsort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## counting sort
        counting_sort(alist4, 1000)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    countsort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
    ######## counting sort
        counting_sort(alist5, 1250)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    countsort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## counting sort
        counting_sort(alist6, 2500)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    countsort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## counting sort
        counting_sort(alist7, 3570)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    countsort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## counting sort
        counting_sort(alist8, 5000)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    countsort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## counting sort
        counting_sort(alist9, 6250)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    countsort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## counting sort
        counting_sort(alist10, 7500)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    countsort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## counting sort
        counting_sort(alist11, 8750)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    countsort_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## counting sort
        counting_sort(alist12, 10000)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    countsort_avglist.append(average)

    print(countsort_avglist)

benchmark_countingsort()