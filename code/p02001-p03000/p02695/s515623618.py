import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(1000000) 
ans = 0
def main():
    N, M, Q = map(int, readline().split())
    query = []
    for _ in range(Q):
        a, b, c, d = map(int, readline().split())
        a -= 1
        b -= 1
        query.append((a, b, c, d))

    def slv(A):    
        s = 0
        for a, b, c, d in query:
            if A[b]-A[a] == c:
                s += d
        return s
    #数列Aを構築
    #数列Aを構築できたら計算処理
    from collections import deque 
    A = deque()
    def dfs(p):
        global ans
        if p == N:
            s = 0
            for a, b, c, d in query:
                if A[b]-A[a] == c:
                    s += d
            ans = max(s, ans)
            return
        if len(A) == 0:
            k = 1
        else:
            k = A[p-1]
        for i in range(k, M+1):
            A.append(i)
            dfs(p+1)
            A.pop()
    dfs(0)
    print(ans)
if __name__ == '__main__':
    main()
