def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
A = iil()
ans = 0
if 1 in A:
    num = A.index(1)
    ans += num
    A = A[num:]
else:
    print(-1)
    exit()
f = 0
#print(A,ans)
for i in range(2,n+1):
    try:
        d = A.index(i,f)
    except AttributeError:
        ans += len(A[f+1:])
        print(ans)
        exit()
    except ValueError:
        ans += len(A[f+1:])
        print(ans)
        exit()
    ans += d - f - 1
    f = d
print(ans)