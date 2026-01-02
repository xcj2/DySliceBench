def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
import copy

n,k = getList()
buff = []
for i in range(n):
    buff.append(getList())

def calc(width, cutbuf, k):
    nn= len(cutbuf)
    cutbuf.sort(key=lambda x: x[1])
    ret = 10**19
    for ii in range(nn-k+1):
        tmptmp = abs(cutbuf[ii][1] - cutbuf[ii+k-1][1])
        #print("here")
        if ret > tmptmp:
            #print("here")
            ret = tmptmp
    #print(ret, cutbuf)
    return ret*width
buff.sort()
ans = 10**19
for i in range(n):
    for j in range(i+1, n):
        width = abs(buff[i][0] - buff[j][0])
        tmp = calc(width, buff[i:j+1], k)

        if ans > tmp:
            ans = tmp

print(ans)