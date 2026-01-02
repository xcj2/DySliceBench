t=[]
for i in range(3):
    t.append([int(i) for i in input().split()])
n = int(input())
lst = []
for i in range(n):lst+=[int(input())]
def ligne(i):
    for j in range(3):
        if not t[i][j] in lst:
            return False
    return True
def col(j):
    for i in range(3):
        if not t[i][j] in lst:
            return False
    return True
def diag1():
    for i in range(3):
        if not t[i][i] in lst:
            return False
    return True
def diag2():
    for i in range(3):
        if not t[2-i][i] in lst:
            return False
    return True
ans = False
for i in range(3):
    ans = ans or ligne(i)
    ans = ans or col(i)
ans  = ans or diag1() or diag2()
if ans :
    print("Yes")
else:
    print("No")