def calculate(S):
    result = []

    rNum = 0
    lNum = 0
    for i in range(len(S)):
        if S[i] == "L":
            lNum = lNum + 1
        else:
            rNum = rNum + 1

        if i > 0:
            if (S[i] == "R") and (S[i-1] == "L"):
                result.append([rNum-1,lNum])
                rNum = 1
                lNum = 0

        if i == len(S) - 1:
            result.append([rNum,lNum])

    return result

def constructZero(n):
    res = ""
    for i in range(n):
        res = res + "0 "
    return res

def calculate2(arr):
    ret = ""
    for index in range(len(arr)):

        arr[index][0]
        arr[index][1]

        s1 = constructZero(arr[index][0]-1)
        s2 = constructZero(arr[index][1]-1)

        if arr[index][0] % 2 == 0:
            l1 = arr[index][0]//2
        else:
            l1 = (arr[index][0] + 1) // 2

        g1 = arr[index][0] - l1

        if arr[index][1] % 2 == 0:
            l2 = arr[index][1]//2
        else:
            l2 = (arr[index][1] + 1) // 2

        g2 = arr[index][1] - l2


        ret = ret + s1 + str(l1 + g2) + " " + str(l2 + g1)+ " " + s2

    return ret

S = input()
result = calculate(S)
ret = calculate2(result)
print(ret)