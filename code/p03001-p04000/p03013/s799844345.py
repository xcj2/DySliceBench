def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,m = iim()
broke = []
for j in range(m):
    broke.append(ii())
if n > 1:
    num = [1]
    if len(broke) and broke[0] == 1:
        num.append(0)
        broke.pop(0)
    else:
        num.append(1)

    for i in range(2,n+1):
        if len(broke) and broke[0] == i:
            num.append(0)
            broke.pop(0)
        else:
            num.append((num[-1]+num[-2])%1000000007)
    print(num[-1])
else:
    print(1)
