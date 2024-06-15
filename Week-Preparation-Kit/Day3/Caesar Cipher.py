#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    alphabet = string.ascii_lowercase
    k = k % 26
    shifted_alphabet = alphabet[k:] + alphabet[:k]
    table = str.maketrans(alphabet, shifted_alphabet)
    s = s.translate(table)
    alphabet = string.ascii_uppercase
    shifted_alphabet = alphabet[k:] + alphabet[:k]
    table = str.maketrans(alphabet, shifted_alphabet)
    return s.translate(table)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
