import sys
def main():
    input = sys.stdin.readline
    N = int(input())
    E = [[] for _ in range(N)]
    for i in range(N-1):
        a, b = map(int, input().split())
        a, b = a-1, b-1
        E[a].append((b,i))
        E[b].append((a,i))
    
    def dfs(s, g):
        par = [(-1,-1)] * N
        par[s] = (s,-1)
        stack = [s]
        while stack:
            v = stack.pop()
            for to, i in E[v]:
                if par[to][0] >= 0: continue
                par[to] = (v, i)
                if to == g: break
                stack.append(to)
        r = set()
        v = g
        while v != s:
            v, i = par[v]
            r.add(i)
        return r
    
    M = int(input())
    path = [None] * M
    for i in range(M):
        u, v = map(int, input().split())
        u, v = u-1, v-1
        path[i] = dfs(u, v)

    def calc(s): return 1<<(N-1-len(s))

    i_ans = 0
    for p in range(1, 1<<M):
        is_odd = 0
        s = set()
        for i in range(M):
            if p&1:
                s |= path[i]
                is_odd ^= 1
            p >>= 1
        if is_odd: i_ans += calc(s)
        else: i_ans -= calc(s)

    print((1<<(N-1)) - i_ans)

if __name__ == '__main__':
    main()