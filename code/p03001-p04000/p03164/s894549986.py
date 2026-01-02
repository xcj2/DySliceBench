
class obj:
    def __init__(self,w,v):
        self.w = w
        self.v = v
        self.r = v/w

x = input().split()
N = int(x[0])
M = int(x[1])
item = []
item = []
for i in range(N):
    x = input().split()
    item.append(obj(int(x[0]),int(x[1])))

maxV = 0


def getKey(x):
    return x.r


item.sort(key=getKey, reverse=True)
	
def Bound(i, C):	# object i -> n-1, capacity = C
    global item, N
    
    sw = 0
    sv = 0
    j = i
    f = 1.0
    while j < N and f == 1.0:
        wj = min(C-sw, item[j].w)
        f = float(wj)/item[j].w
        sw += f*item[j].w
        sv += f*item[j].v
        j += 1
    return sv



def dfsv4(i, sumW, sumV):
    """prning bounding, branching"""
    global maxV, item, N, M
    if i == N:
        if sumW <= M:
            maxV = max(maxV, sumV)
    else:   
        temp1 = Bound(i+1, M-sumW) + sumV
        temp2 = Bound(i,M-sumW) + sumV
        is1 = False

        if temp1 > temp2:
            is1 = True

        if is1:
            if temp1 > maxV:
                dfsv4(i+1, sumW, sumV)
            if sumW + item[i].w <= M:
                if temp2 > maxV:
                    dfsv4(i+1, sumW+item[i].w, sumV+item[i].v)
        else:
            if sumW + item[i].w <= M:
                if temp2 > maxV:
                    dfsv4(i+1, sumW+item[i].w, sumV+item[i].v)
            if temp1 > maxV:
                dfsv4(i+1, sumW, sumV)


dfsv4(0,0,0)

print(maxV)





    
