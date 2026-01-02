from heapq import heappush,heappop

def int_raw():
    return int(input())

def ss_raw():
    return input().split()

def ints_raw():
    return list(map(int,ss_raw()))

X,Y,Z,K = ints_raw()

A = ints_raw()
B= ints_raw()
C= ints_raw()
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

arg_hash = {}

def main():
    Q = []
    heappush(Q,(-A[0]-B[0]-C[0],0,0,0))
    arg_hash[(0,0,0)]=1
    for k in range(K):
        ans = heappop(Q)
        print(-ans[0])
        a,b,c = ans[1:]

        argA = (a+1,b,c)
        if a < X-1 and (not argA in arg_hash):
            arg_hash[argA]=1
            heappush(Q,(-A[a+1]-B[b]-C[c],)+argA)
        argB = (a,b+1,c)
        if b < Y-1 and (not argB in arg_hash):
            arg_hash[argB]=1
            heappush(Q, (-A[a]-B[b+1]-C[c],)+argB)
        argC = (a,b,c+1)
        if c < Z-1 and (not argC in arg_hash):
            arg_hash[argC]=1
            heappush(Q,(-A[a]-B[b]-C[c+1],)+argC)
        
main()
