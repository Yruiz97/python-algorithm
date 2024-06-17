if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max1, max2 = arr[0], -100
    for i in range(1, n):
        if max2 < arr[i]:
            if max1 < arr[i]:
                max2, max1 = max1, arr[i]
            elif max1 > arr[i]:
                max2 = arr[i]
    print(max2)