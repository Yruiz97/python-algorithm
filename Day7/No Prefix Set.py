#!/bin/python3

import math
import os
import random
import re
import sys
import bisect
#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

def noPrefix(words):
    arr = []
    for s in words:
        p = bisect.bisect_right(arr, s)
        if p >= 1 and s.startswith(arr[p - 1]):
            print("BAD SET")
            print(s)
            return

        if p < len(arr) and arr[p].startswith(s):
            print("BAD SET")
            print(s)
            return

        arr.insert(p, s)

    print("GOOD SET")

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
