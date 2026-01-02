def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

n,k = iim()
A = iil()
'''
A = [0]*200000
上記でtryしても41回で全て明るさ200000になる
'''

def imos(l):
    n = len(l)
    tmp = [0]*n
    for i,item in enumerate(l):
        l = max(0,i-item)
        r = min(n-1,i+item)
        tmp[l] += 1
        if r+1 < n:
            tmp[r+1] -= 1
    for i in range(1,n):
        tmp[i] += tmp[i-1]
    return tmp

for _ in range(min(k,100)):
    A = imos(A)
#    print(_,min(A))

print(*A)