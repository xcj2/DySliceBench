def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
import bisect
A,B,Q = getList()
temple = []
shrine = []
for i in range(A):
    temple.append(getN())

for i in range(B):
    shrine.append(getN())

temple.sort()
shrine.sort()

near_sh = []
for t in temple:
    a = bisect.bisect_left(shrine, t)
    if a == 0:
        l = -1000000000000
    else:
        l = shrine[a-1]
    if a == B:
        r = 1000000000000
    else:
        r = shrine[a]
    near_sh.append((l,r))

def calc(x, a, direction):
    #l=1
    try:
        near_temp = temple[a-direction]
    except:
        return 100000000000
    cost_outshrine = abs(x-near_sh[a-direction][1-direction])
    cost_inshrine = abs(x-near_temp)
    if cost_inshrine < abs(near_temp - near_sh[a-direction][0+direction]):
        #print("cost", near_sh[a - direction][0 + direction], cost_inshrine)
        cost_inshrine = (abs(near_temp - near_sh[a-direction][0+direction])) + min(cost_inshrine, abs(x- near_sh[a - direction][0 + direction]))

    #print("inoput", cost_inshrine,cost_outshrine,a,direction)
    return min(cost_inshrine, cost_outshrine)

#print(shrine)
#print(temple)
#print(near_sh)
for i in range(Q):
    x = getN()
    a = bisect.bisect_left(temple,x)
    if a != 0:
        cost_l = calc(x,a,1)
    else:
        cost_l = 1000000000000
    if a != A:
        cost_r = calc(x,a,0)
    else:
        cost_r = 1000000000000

    print(min(cost_l, cost_r))
