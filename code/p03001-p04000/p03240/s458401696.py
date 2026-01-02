import sys
input = sys.stdin.readline

def readlines(n):
    for _ in range(n):
        x, y, h = map(int, input().split())
        yield x, y, h

def h_check(lines, cx, cy):
    for x, y, h in lines:
        if h > 0:
            yield h + abs(x - cx) + abs(y - cy)

def match(cx, cy, H, lines):
    for x, y, h in lines:
        yield max(H - abs(x - cx) - abs(y - cy), 0) == h

def main():
    n = int(input())
    lines = list(readlines(n))
    for cx in range(101):
        for cy in range(101):
            res = set(h_check(lines, cx, cy))
            if len(res) == 1:
                H = res.pop()
                if all(match(cx, cy, H, lines)):
                    print(cx, cy, H)
                    return

main()

