import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def div2(h, w):
    if w % 2 and h % 2:
        if w < h: w, h = h, w
        return h * (w // 2), h * (w // 2 + 1)
    else:
        return h * w // 2, h * w // 2

def main():
    h, w = MI()
    a = []
    for w1 in range(1, w // 2 + 1):
        p1 = w1 * h
        p2, p3 = div2(h, w - w1)
        a.append(max(p1, p2, p3) - min(p1, p2, p3))
    h, w = w, h
    for w1 in range(1, w // 2 + 1):
        p1 = w1 * h
        p2, p3 = div2(h, w - w1)
        a.append(max(p1, p2, p3) - min(p1, p2, p3))
    print(min(a))

main()
