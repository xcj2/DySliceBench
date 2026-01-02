from collections import namedtuple

Point = namedtuple('Point', ('x', 'y'))

def main():
    n = int(input())
    reds = []
    blues = []

    for _ in range(n):
        x, y = map(int, input().split())
        reds.append(Point(x, y))

    for _ in range(n):
        x, y = map(int, input().split())
        blues.append(Point(x, y))
    
    print(solve(reds, blues))

def solve(reds, blues):
    cnt = 0
    r = reds.copy()

    for b in sorted(blues):
        i = find_pair(r, b.x, b.y)
        if i is not None:
            del r[i]
            cnt += 1
        pass
    
    return cnt

def find_pair(reds, x, y):
    t = None
    for i, p in enumerate(reds):
        if p.x < x and p.y < y:
            if t is None:
                t = i
            elif p.y > reds[t].y:
                t = i
    return t

main()
