dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

INF = float('inf')
MOD = 1000000000 + 7

def LI(): return [int(x) for x in input().split(" ")]
def LS(): return [str(x) for x in input().split(" ")]
def ItoS(L): return [str(x) for x in L]
def StoI(L): return [int(c) for c in L]

def check(n):
    l = len(str(n))
    for ele in list(str(n)):
        if ele != "9":
            return False

    return True

def Sum(n):
    L = list(str(n))
    sum = 0
    for ele in L:
        sum += int(ele)

    return sum

def solve():
    while 1:
        try:
            n = int(input())
            if 1 <= n <= 9:
                print(n)
                raise EndLoop

            l = len(str(n))

            tmp = str(n)[0]

            if check(n):
                print(9 * l)
            else:
                print(max(Sum(n), 9 * (l - 1) + int(tmp) - 1))
            break
        except:
            break

solve()