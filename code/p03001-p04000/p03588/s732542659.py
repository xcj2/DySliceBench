def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
cond = []
for i in range(n):
    cond.append(iil())
cond = sorted(cond)
#print(cond)
cand = (cond[0][1]+1)+(cond[0][0]-1)
for i in range(1,n):
#    print(cond[i])
    if cond[i][0] - cond[i-1][0] >= cond[i-1][1]-cond[i][1]:
        cand = (cond[i][1]+1)+(cond[i][0]-1)
    else:
        cand -= (cond[i-1][1]-cond[i][1]) - (cond[i][0] - cond[i-1][0])
print(cand)