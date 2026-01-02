import math


def gcdf(a, b):
    if a > b:
        a, b = b, a
    if b%a==0:
        return a
    return gcdf(a, b % a)


def f(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append(i)

    if temp != 1:
        arr.append(temp)

    if arr == []:
        arr.append(n)

    return arr


def main():
    # return
    # N = int(input())
    # N,= [int(a) for a in input().split()]
    A, B = [int(a) for a in input().split()]

    gcd = gcdf(A, B)

    if gcd == 1:
        print(1)
    else:
        print(len(f(gcd)) + 1)


if __name__ == "__main__":
    main()
