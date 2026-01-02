import sys
from collections import deque

stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    n, m = nm()
    friends = [set() for _ in range(n)]
    for i in range(m):
        a, b = nm()
        friends[a - 1].add(b - 1)
        friends[b - 1].add(a - 1)

    groups = []
    in_group = [False] * n
    for i in range(n):
        if in_group[i]:
            continue
        d = deque(friends[i])
        group = [i]
        in_group[i] = True
        while d:
            c = d.pop()
            if in_group[c]:
                continue
            group.append(c)
            in_group[c] = True
            for friend in friends[c]:
                if not in_group[friend]:
                    d.append(friend)
        groups.append(group)

    ans = 0
    for group in groups:
        ans = max(ans, len(group))
    print(ans)


if __name__ == '__main__':
    main()
