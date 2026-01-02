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
    a = lmi()
    a.sort()
    ans = 1
    for i in range(n):
        ans *= a[i]
        if ans > 10**18:
            break
    else:
        print(ans)
        return
    print(-1)
    return

if __name__ == "__main__":
    main()
