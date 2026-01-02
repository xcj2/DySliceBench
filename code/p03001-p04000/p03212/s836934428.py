import sys
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
INF = 10 ** 18
MOD = 10 ** 9 + 7

counter = 0
def main():
    N = II()
    def dp(number, has_seven, has_five, has_three):
        global counter
        if int(number+'7') <= N:
            if has_five and has_three:
                counter += 1
            dp(number+'7', True, has_five, has_three)
        if int(number+'5') <= N:
            if has_seven and has_three:
                counter += 1
            dp(number+'5', has_seven, True, has_three)
        if int(number+'3') <= N:
            if has_seven and has_five:
                counter += 1
            dp(number+'3', has_seven, has_five, True)
    dp('',False,False,False)
    print(counter)

main()