#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    start,xsum=0,0
    for i in range(n):
        xsum+=petrolpumps[i][0]-petrolpumps[i][1]     #Calculating the difference and adding to the sum
        if xsum<0:          #If sum becomes negative, that means we cannot complete the loop
            start=i+1       #So start from the next index
            xsum=0          #Reset the sum
    return start

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
