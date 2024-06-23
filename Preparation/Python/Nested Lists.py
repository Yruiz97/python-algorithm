if __name__ == '__main__':
    result = {}
    min1, min2 = 999999, 999999
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in result:
            result[score].append(name)
        else:
            result[score] = [name]
        if score < min1:
            min2 = min1
            min1 = score
        elif score > min1 and score < min2:
            min2 = score
    result[min2].sort()
    for name in result[min2]:
        print(name)