import sys
sys.setrecursionlimit(10**6)
    
def main():
    N = int(input())
    d = {}
    for _ in range(N-1):
        a, b = map(int, input().split())
        if a in d:
            d[a].append(b)
        else:
            d[a] = [b]
        if b in d:
            d[b].append(a)
        else:
            d[b] = [a]
    v = set()
    v.add(1)
    l = []
    def dfs(n):
        if n == N:
            l.append(n)
            return True
        for i in d[n]:
            if i not in v:
                v.add(i)
                if dfs(i):
                    l.append(n)
                    return True
        return False
    dfs(1)
    l.reverse()
    v = set()
    if len(l) % 2 == 0:
        half = len(l) // 2 - 1
    else:
        half = len(l) // 2
    v.add(l[half])
    s = l[half+1]
    v.add(s)
    def dfs2(n):
        r = 1
        for i in d[n]:
            if i not in v:
                v.add(i)
                r += dfs2(i)
        return r
    x = dfs2(s)
    if N - x > x:
        return 'Fennec'
    else:
        return 'Snuke'
print(main())
