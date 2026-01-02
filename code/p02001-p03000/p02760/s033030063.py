#横判定
def judgehol(a, b):
    for i in range(3):
        flag = [False, False, False]
        for j in range(3):
            if a[i][j] in b:
                flag[j] = True
        if flag[0] and flag[1] and flag[2]:
            break
    return flag[0] and flag[1] and flag[2]

#縦判定
def judgever(a, b):
    for j in range(3):
        flag = [False, False, False]
        for i in range(3):
            if a[i][j] in b:
                flag[i] = True
        if flag[0] and flag[1] and flag[2]:
            break
    return flag[0] and flag[1] and flag[2]


#斜め判定
def judgecross(a, b):
    if a[0][0] in b and a[1][1] in b and a[2][2] in b:
        return True
    elif a[0][2] in b and a[1][1] in b and a[2][0] in b:
        return True
    else:
        return False


a1 = list(map(int,input().split()))
a2 = list(map(int,input().split()))
a3 = list(map(int,input().split()))
a = [a1, a2, a3]

n = int(input())

b = [int(input()) for i in range(n)]


if judgehol(a, b) or judgever(a, b) or judgecross(a, b):
    print('Yes')
else:
    print('No')
