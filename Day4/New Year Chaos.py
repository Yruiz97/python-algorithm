#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    counter = 0
    current_position = len(q) - 1
    bribes = 0

    while current_position >= 0:
        current = q[current_position]
        order_position = current_position + 1

        bribes = current - order_position

        if bribes >= 3:
            print("Too chaotic")
            return

        briber_position = current - 2

        for compare_position in range(max(0, briber_position), current_position):
            compare = q[compare_position]
            if compare > current:
                counter += 1

        current_position -= 1
    print(counter)
    
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
