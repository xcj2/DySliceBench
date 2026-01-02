import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    def main():
        x, n = map(int, input().split())
        if n == 0:
            return x
        else:
            p = list(map(int, input().split()))


            cur = 0
            if x not in p:
                return x
            
            while True:
                if x-cur not in p:
                    return x-cur
                if x+cur not in p:
                    return x+cur

                cur+=1
    print(main())


resolve()