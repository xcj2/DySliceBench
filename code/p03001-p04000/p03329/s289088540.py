import collections

def main():
    n = int(input())
    c = search(n)
    print(c)

def search(n):
    q = collections.deque()
    q.append((0, n, []))

    while q:
        cnt, rest, lst = q.popleft()
        for c in candidates(rest):
            if c == rest:
                return cnt + 1
            elif c < rest:
                q.append((cnt + 1, rest - c, lst + [c]))

def candidates(n):
    if n < 6:
        return [1]
    elif n < 9:
        return [6, 1]
    else:
        s = []
        p = 9
        while p <= n:
            p *= 9
        s.append(p // 9)

        q = 6
        while q <= n:
            q *= 6
        s.append(q // 6)

        return s

main()