import heapq
from collections import defaultdict
import sys
import bisect
input = sys.stdin.readline

n = int(input())
#####単位元######
ide_ele = -1

#num:n以上の最小の2のべき乗
num =2**((n-1).bit_length())
seg=[ide_ele]*(2*num)

def init(init_val):
    #set_val
    for i in range(n):
        seg[i+num-1]=init_val[i]    
    #built
    for i in range(num-2,-1,-1) :
        seg[i]=max(seg[2*i+1],seg[2*i+2]) 
    
def update(k,x):
    k += num-1
    seg[k] = x
    while k+1:
        k = (k-1)//2
        seg[k] = max(seg[k*2+1],seg[k*2+2])
    
def query(p,q):
    if q<=p:
        return ide_ele
    p += num-1
    q += num-2
    res=ide_ele
    while q-p>1:
        if p&1 == 0:
            res = max(res,seg[p])
        if q&1 == 1:
            res = max(res,seg[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = max(res,seg[p])
    else:
        res = max(max(res,seg[p]),seg[q])
    return res
    
def main():
    used = defaultdict(int)
    a = [int(input()) for i in range(n)]
    b = sorted(a)
    for i in range(n):
        a[i] = bisect.bisect_left(b,a[i])
    
    tank = [a[0]]
    used[a[0]] = 1
    update(a[0],a[0])
    
    for i in range(1,n):
        while True:
            if used[tank[0]] > 0:
                break
            else:
                heapq.heappop(tank)
        #塗り替え
        if tank[0] < a[i]:
            ma = query(0,a[i])
            
            used[ma] -= 1
            heapq.heappush(tank,a[i])
            used[a[i]] += 1
            if used[ma] == 0:
                update(ma,-1)
        else:
            heapq.heappush(tank,a[i])
            used[a[i]] += 1
        update(a[i],a[i])

    res = 0
    for e in tank:
        if used[e] > 0:
            res += 1
            used[e] -= 1
    print(res)

if __name__ == '__main__':
    main()
