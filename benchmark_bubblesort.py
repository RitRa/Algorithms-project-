# importing the random numbers
from randomnumber import *


# code sourced from http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


import time

global bubble_avglist
bubble_avglist = []
num_runs = 10
results = []
# benchmark bubble function

def benchmark_bubble():# import time module
    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## bubblesort
        bubbleSort(alist)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    # round to 3 decimals
    average = round(average, 3)
    bubble_avglist.append(average)


    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## bubblesort
        bubbleSort(alist1)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    # round to 3 decimals
    average = round(average, 3)
    bubble_avglist.append(average)


    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## bubblesort
        bubbleSort(alist2)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    # round to 3 decimals
    average = round(average, 3)
    bubble_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## bubblesort
        bubbleSort(alist3)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    # round to 3 decimals
    average = round(average, 3)
    bubble_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## bubblesort
        bubbleSort(alist4)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    # round to 3 decimals
    average = round(average, 3)
    bubble_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## bubblesort
        bubbleSort(alist5)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    # round to 3 decimals
    average = round(average, 3)
    bubble_avglist.append(average)


    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## bubblesort
        bubbleSort(alist6)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    # round to 3 decimals
    average = round(average, 3)
    bubble_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## bubblesort
        bubbleSort(alist7)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    # round to 3 decimals
    average = round(average, 3)
    bubble_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## bubblesort
        bubbleSort(alist8)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    # round to 3 decimals
    average = round(average, 3)
    bubble_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## bubblesort
        bubbleSort(alist9)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    # round to 3 decimals
    average = round(average, 3)
    bubble_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## bubblesort
        bubbleSort(alist10)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    # round to 3 decimals
    average = round(average, 3)
    bubble_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## bubblesort
        bubbleSort(alist11)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    # round to 3 decimals
    average = round(average, 3)
    bubble_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## bubblesort
        bubbleSort(alist12)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    # round to 3 decimals
    average = round(average, 3)
    bubble_avglist.append(average)

    for r in range(num_runs):
        # start timer
        start_time = time.time()
        ######## bubblesort
        bubbleSort(alist13)
        end_time = time.time()
        time_elapsed= end_time - start_time
        results.append(time_elapsed)
    b = sum(results)
    average = (b/num_runs)
    # round to 3 decimals
    average = round(average, 3)
    bubble_avglist.append(average)    
    print(bubble_avglist)

    #return bubble_avglist

benchmark_bubble()