from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
def I(): return int(stdin.readline().rstrip())
def LI(): return list(map(int,stdin.readline().rstrip().split()))

def judge(x,y,a,bit):
    for i in range(len(a)):
        if bit&(1<<i):
            for j in range(a[i]):
                if ((bit>>x[i][j])&1)^y[i][j]:
                    return False
    return True

n = I()
a = []
x = []
y = []
for i in range(n):
    A = I()
    a.append(A)
    xt = []
    yt = []
    for _ in range(A):
        tmp = LI()
        xt.append(tmp.pop(0)-1)
        yt.append(tmp.pop(0))
    x.append(xt)
    y.append(yt)

ans = 0
length = 2**n
for i in range(length):
    result = judge(x,y,a,i)
    if result:
        ans = max(ans,bin(i).count('1'))
    
print(ans)