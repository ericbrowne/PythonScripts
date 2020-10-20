## Kadane's Algorithm for solving Max subarray problem ##


import math


## Got from Google
def maxSumSubArray(Array):
    n = A.size()
    local_max = 0
    global_max = -math.inf

    for i in range(0,n):
        local_max = max(A[i], A[i] + local_max)
        if (local_max > global_max):
            global_max = local_max

    return global_max


## Got from Zoom lecture

def maxsumsubarra(Array):
    max_sum = 0
    sum = 0

    for j in range(0, len(Array)):
        if sum < 0:
            sum = 0
            start = j
        sum += array[j]
        if sum > max_sum:
            max_sum = sum
            end = j
            max_start = start
    return max_sum
