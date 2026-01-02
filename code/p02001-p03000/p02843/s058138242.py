def two_int():
    N, K = map(int, input().split())
    return N,K

def one_int():
    return int(input())

def one_str():
    return input()

def many_int():
    return list(map(int, input().split()))

N=one_int()

num=int(N/100) 

amari = N%100

def dfs(now, count, max_count):
    if count==max_count:
        if now+(100*max_count) == N:
            return 1
        else:
            return 0
    else:
        ret=[]
        for i in range(6):
            if (max_count-count-1)*5 + i<N:
                dfs(now+i, count+1, max_count ) 
        return ret

if num*5 < amari:
    print(0)
else:
    print(1)
    

