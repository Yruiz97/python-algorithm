import numpy

arr = [float(x) for x in input().split(" ")]
x = float(input())

print(numpy.polyval(arr, x))