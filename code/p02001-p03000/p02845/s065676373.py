import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    md = 10 ** 9 + 7
    n = int(input())
    aa = LI()
    cnt = [0] * 100005
    check = [0] * 100005
    zero = 0
    ans = 1
    for a in aa:
        if a == 0:
            zero += 1
        else:
            if cnt[a - 1] == 0:
                print(0)
                exit()
            ans *= cnt[a - 1]
            ans %= md
            cnt[a - 1] -= 1
        cnt[a] += 1
        check[a] += 1
        if check[a] > 3:
            print(0)
            exit()
    if zero == 1:
        ans *= 3
    else:
        ans *= 6
    if sum(cnt) == zero:
        print(ans % md)
    else:
        print(0)

main()
