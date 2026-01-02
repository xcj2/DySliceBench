import sys
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def li(): return list(input().rstrip())
def debug(*args, sep=" ", end="\n"): print("debug:", *args, file=sys.stderr, sep=sep, end=end) if not __debug__ else None
def exit(*arg): print(*arg); sys.exit()
# template

def main():
    n = ii()
    l = []
    r = []
    for i in range(n):
        a, b = mi()
        l.append(2 * a)
        r.append(2 * b)
    # print(l)
    l.sort()
    r.sort()
    if n % 2 == 0:
        ll = (l[n // 2] + l[n // 2 - 1]) // 2
        rr = (r[n // 2] + r[n // 2 - 1]) // 2
    else:
        ll = l[n // 2]
        rr = r[n // 2]
    # print(ll, rr)
    if n % 2 == 0:
        print(rr - ll + 1)
    else:
        print(rr // 2 - ll // 2 + 1)
    return

if __name__ == "__main__":
    main()
