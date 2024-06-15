#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    stack = []
    pair = {
        '}': '{',
        ']': '[',
        ')': '('
    }
    for bracket in s:
        if bracket == '{' or bracket == '[' or bracket == '(':
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return "NO"
            last = stack[len(stack) - 1]
            if pair[bracket] == last:
                stack.pop()
            else:
                return "NO"
    if len(stack) == 0:
        return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
