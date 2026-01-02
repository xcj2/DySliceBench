import sys
import math
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def li(): return list(input().rstrip())
def debug(*args, sep=" ", end="\n"): print("debug:", *args, file=sys.stderr, sep=sep, end=end) if not __debug__ else None
def exit(*arg): print(*arg); sys.exit()
# template

def make_devisor(n: int):
    x = n
    ret = []
    for i in range(2, int(math.sqrt(n)) + 1):
        cnt = 0
        while x % i == 0:
            cnt += 1
            x //= i
        if cnt != 0:
            ret.append(cnt)
    if x != 1:
        ret.append(1)
    return ret

def main():
    n = ii()
    a = make_devisor(n)
    # print(a)
    ans = 0
    for x in a:
        t = -1
        while (t + 2) * (t + 1) // 2 <= x:
            t += 1
        ans += t
    print(ans)
    return

if __name__ == "__main__":
    main()
