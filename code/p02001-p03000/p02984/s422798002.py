def calculate(N, arr, S):
    result = []
    tmp = 0
    for i in range(len(arr)):
        if i % 2 == 1:
            tmp += arr[i] * 2

    x0 = S - tmp

    result.append(x0)

    for i in range(1, N):
        result.append(arr[i - 1] * 2 - result[i - 1])

    return result


def calculate2(i, arr):
    # 取偶数项
    return sum(arr[::2]) * 2


def calculateTotaAmount(arr):
    return sum(arr)


def printArr(arr):
    result = ""
    for i in range(len(arr)):
        result += str(arr[i]) + " "

    return result



N = int(input())

S = input().split(" ")
aArr = [int(s) for s in S]

result = calculate(N, aArr, calculateTotaAmount(aArr))
print(" ".join([str(s) for s in result]))
