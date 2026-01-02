import math
S = input()

def convert(arr):
    H = []
    for value in arr:
        H.append(int(value))
    return H

def fix0(arr):
    count = 0
    for i in range(1,len(arr)):
        if arr[i] == arr[i-1]:
            arr[i] = math.fabs(arr[i-1] - 1)
            count = count + 1
    return count

def fix1(arr):
    count = 0
    if arr[0] == arr[1]:
        count = count + 1

    if len(arr) > 2:
        for i in range(2,len(arr)):
            if arr[i] == arr[i-1]:
                arr[i] = math.fabs(arr[i-1] - 1)
                count = count + 1
    return count

def compare(x,y):
    if x < y:
        return x
    else:
        return y

def main(arr):
    if len(arr) > 1:
        # 0 fixed
        # 1 fixed
        count1 = fix0(arr.copy())
        count2 = fix1(arr.copy())
        return compare(count1,count2)
    else:
        return 0


print(main(convert(S)))




