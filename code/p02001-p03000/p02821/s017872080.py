import bisect


def GETCOUNT(A,border,N):
    count = 0
    for i in range(N):
        index = bisect.bisect_left(A,border-A[i])
        count +=N-index
    return count

def get_ans(A,smt,border,N):
    sm=0
    for i in range(N):
        index = bisect.bisect_left(A,border-A[i])
        sm+=(N-index)*A[i]

        if index==N:
            continue
        sm+=smt[index]

    return sm


def resolve():
    N,M = map(int,input().split())
    A=[int(i) for i in input().split()]
    A.sort()

    smt=[0]*N
    smt[-1]=A[-1]
    for i in range(N-2,-1,-1):
        smt[i]=smt[i+1]+A[i]

    lid = 0 
    lco = N*N

    rid = A[-1]*2 +1
    rco = 0

    center =0
    center_count =0
    cc=0
    while True:
        center=(lid+rid)//2
        center_count=GETCOUNT(A,center,N)


        if center_count > M:
            lid = center
            lco = center_count
        else:
            rid = center
            rco = center_count
        
        if rid == lid+1 and rco != M and lco !=M:
            cc=lid*(lco - M)
            center = lid
            break



        if center_count == M:
            break
    
    print(get_ans(A,smt,center,N)-cc)








if __name__ == "__main__":
    resolve()