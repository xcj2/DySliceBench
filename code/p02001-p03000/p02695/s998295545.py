def solve():
    N,M,Q = map(int,input().split())
    global info
    info = []
    for _ in range(Q):
        a,b,c,d = map(int,input().split())
        a -= 1
        b -= 1
        info.append([a,b,c,d])

    print(dfs(list(),M,N))

def dfs(A,M,N):
    if len(A) == N:
        return calcPoint(A)
    
    res = 0
    prev = A[-1] if len(A) > 0 else 1
    for i in range(prev,M+1):
        A.append(i)
        res = max(res,dfs(A,M,N))
        A.pop()
    
    return res

def calcPoint(A):
    result = 0
    for a,b,c,d in info:
        if A[b] - A[a] == c:
            result += d
    return result
                
if __name__ == '__main__':
    solve()