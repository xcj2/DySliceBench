import sys

sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return list(map(int, sys.stdin.readline().split()))
def II(): return int(sys.stdin.readline())
def LS(): return list(map(list, sys.stdin.readline().split()))
def S(): return list(sys.stdin.readline())[:-1]

def main():
    t1, t2 = LI()
    a1, a2 = LI()
    b1, b2 = LI()

    if a1 < b1:
        tmp = b1
        b1 = a1
        a1 = tmp

        tmp = b2
        b2 = a2
        a2 = tmp

    l1 = (a1 - b1) * t1
    l2 = (a2 - b2) * t2
    l3 = l1 + l2

    if l3 == 0:
        print("infinity")
        return
    if l3 > 0:
        print(0)
        return
    ans = 1
    if l1 % (-l3) == 0:
        print(ans + 2 * (l1 // (-l3)) - 1)
        return
    print(ans + 2 * (l1 // (-l3)))






if __name__ == '__main__':
    main()