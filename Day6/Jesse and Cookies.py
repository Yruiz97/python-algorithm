#!/bin/python3

import math
import os
import random
import re
import sys
import heapq
#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(K, cookies):
    heapq.heapify(cookies)

    operations = 0
    if not len(cookies):
        return -1
    
    while len(cookies):
        c1 = heapq.heappop(cookies)
        if c1 < K:
            operations +=1
            if len(cookies):
                c2 = heapq.heappop(cookies)
                n = c1 + 2*c2  #formulating the sweetness acc to question
                heapq.heappush(cookies, n)
            else:
                return -1
        else:   
            break 
    return operations

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
