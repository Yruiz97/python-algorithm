import numpy

N = int(input())
A = numpy.array([[float(x) for x in input().split()] for i in range(N)])
print(round(numpy.linalg.det(A), 2))