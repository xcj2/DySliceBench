
def nums():
    return list(map(int,input().split(" ")))
def num():
    return int(input())
def yakusu(n):
    res = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            res.add((i,int(n/i)))
    return res
"""
a,b = nums()
if a <= 9 and b <= 9:
    print(a * b)
else:
    print(-1)
"""
"""
n = num()
qq = []
for i in range(10):
    for j in range(10):
        qq.append(i * j)
if n in qq:
    print("Yes")
else:
    print("No")
"""
N = num()
y = yakusu(N)

min = -1

for i in y:
    x,y = i
    if min == -1:
        min = x + y
    elif min > x + y:
        min = x+y

print(min-2)