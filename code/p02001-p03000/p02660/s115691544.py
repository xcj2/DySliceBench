import math
import sys
sys.setrecursionlimit(10**9)

def main():
    N = int(input())

    res = []
    def isP(i):
        if i == 1:
            return False
        for j in res:
            if i % j == 0:
                return False
        return True

    def calc(p):
        mx = math.floor(math.log(N,p))
        # print("mx",mx)
        e_v = pow(p,mx)
        e = 0
        ng = False
        for i in reversed(range(mx)):
            if not ng and N % e_v == 0:
                ng = True
                e = i+1

            if not ng:
                e_v //= p
                e = i+1

        # print("e",e)
        base = -1+math.sqrt(1+8*e)
        return math.floor(base/2)

    tail = []
    ans = 0
    for p in range(1, int(N**0.5)+1):
        tail.append(N//p)
        if N % p == 0 and isP(p):
            res.append(p)
            # print("p",p)

            ans += calc(p)
    for p in tail:
        if N % p == 0 and isP(p):
            res.append(p)
            # print("p",p)

            ans += calc(p)


    print(ans)

if __name__ == "__main__":
  main()