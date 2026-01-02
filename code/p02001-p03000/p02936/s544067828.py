import sys
 
sys.setrecursionlimit(10 ** 6)

def input():
    return sys.stdin.readline().strip()
def main():
    N,Q = map(int,input().split())
    K = [[] for _ in range(N+1)]
    nums = [0 for _ in range(N+1)]

    for _ in range(N-1):
        a,b = map(int,input().split())
        K[a].append(b)
        K[b].append(a)

    for _ in range(Q):
        p, x = map(int, input().split())
        nums[p] += x

    def dfs(now,parent):
        for i in K[now]:
            if i != parent:
                nums[i] += nums[now]
                dfs(i,now)

    dfs(1,0)
    print(*nums[1:])

if __name__ == '__main__':
    main()