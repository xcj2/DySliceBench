n = input()
k = int(input())

def case1(x):
    return (len(x) - 1) * 9 + int(x[0])

def case2(x):
    if (len(x) < 2):
        return 0
    ret = (len(x) - 1) * (len(x) - 2) // 2 * 81
    ret += case1('9' * (len(x) - 1)) * (int(x[0]) - 1)
    for i in range(1, len(x)):
        if x[i] != '0':
            ret += case1(x[i:])
            break
    return ret

def case3(x):
    if (len(x) < 3):
        return 0
    ret = (len(x) - 1) * (len(x) - 2) * (len(x) - 3) // 6 * 729
    ret += case2('9' * (len(x) - 1)) * (int(x[0]) - 1)
    for i in range(1, len(x)):
        if x[i] != '0':
            ret += case2(x[i:])
            break
    return ret

if k == 1:
    print(case1(n))
elif k == 2:
    print(case2(n))
else:
    print(case3(n))