#!/usr/bin/env python3
def solve1(n, r, s, p, t):
    cur = {'r': 0, 's': 0, 'p': 0}
    for c in t:
        prv = cur
        cur = {'r': 0, 's': 0, 'p': 0}
        for x in 'rsp':
            if x == 'r' and c == 's':
                score = r
            elif x == 's' and c == 'p':
                score = s
            elif x == 'p' and c == 'r':
                score = p
            else:
                score = 0
            for y in 'rsp':
                if y != x:
                    cur[x] = max(cur[x], prv[y] + score)
    return max(cur.values())

def solve(n, k, r, s, p, t):
    u = [[] for _ in range(k)]
    for i, c in enumerate(t):
        u[i % k].append(c)
    return sum([solve1(n, r, s, p, u[j]) for j in range(k)])

def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()
    print(solve(n, k, r, s, p, t))
if __name__ == "__main__":
    main()
