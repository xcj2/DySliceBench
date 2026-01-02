import sys

sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return list(map(int, sys.stdin.readline().split()))
def II(): return int(sys.stdin.readline())
def LS(): return list(map(list, sys.stdin.readline().split()))
def S(): return list(sys.stdin.readline())[:-1]

def main():
    s = S()
    for i, v in enumerate(s):
        if i % 2 == 0:
            if v not in ("R", "U", "D"):
                print("No")
                return
        else:
            if v not in ("L", "U", "D"):
                print("No")
                return
    print("Yes")


if __name__ == '__main__':
    main()