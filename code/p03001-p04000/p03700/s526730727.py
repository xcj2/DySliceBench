import math

def ok_check(half, data, num, a, b):
    kari = 0
    for i in range(num):
        nokori = data[i] - half * b
        if nokori > 0:
            kari += math.ceil(nokori / (a - b))
    if kari > half:
        return 0
    else:
        return 1

def check(left, right, data, num, a, b):
    if left == right - 1:
        print(right)
        return
    half = (left + right) // 2
    if ok_check(half, data, num, a, b):
        check(left, half, data, num, a, b)
    else:
        check(half, right, data, num, a, b)

def main():
    num, a, b = map(int, input().split())
    data = [int(input()) for i in range(num)]

    left = 0
    right = max(data) // b + 1
    check(left, right, data, num, a, b)

if __name__ == '__main__':
    main()
