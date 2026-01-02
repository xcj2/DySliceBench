def ccc(n):
    #c(n,2)
    result = (n * (n-1))//2
    return result



def sortString(a):
    a = list(a)
    a.sort()
    return "".join(a)


def calculate(arr):
    if len(arr) == 0:
        return 0

    dict = {}
    for i in range(len(arr)):
        s = sortString(arr[i])
        if dict.get(s) == None:
            dict.setdefault(s,1)
        else:
            dict.__setitem__(s,dict.get(s) + 1)


    sum = 0
    for v in dict.values():
        sum += ccc(v)

    return sum



arr = []

N = int(input())
for i in range(N):
    arr.append(input())


result = calculate(arr)
print(result)