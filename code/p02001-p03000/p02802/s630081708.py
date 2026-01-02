import sys
input = sys.stdin.readline
#from itertools import permutations

def gcd(a: int, b: int):
    """ https://cocodrips.hateblo.jp/entry/2014/03/05/143623
    """
    while b: a, b = b, a%b
    return a

def lcm(a: int, b: int):
    return a * b // gcd(a, b)


def main():
    #N = int(input())
    N,M = map(int, input().split())
    #vP = tuple(map(int, input().split()))
    #vA = list(map(int, input().split()))
    #vA = list(range(1,N+1))
    vS = [input().split() for _ in [0,]*M]
    vN = [False,]*(N+1)
    vW = [0,]*(N+1)

    x,p = 0,0
    for a,s in vS:
        i = int(a)
        v = s=="AC"
        if vN[i]==False:
            if v:
                x += 1
                vN[i] = True
                p += vW[i]
            else:
                vW[i] += 1

    print(x,p)

    #print(l, file=sys.stderr)
    #l //= 2
    #S = input().rstrip()
    #print(S)
    #print(chr(ord(S)+1))
    #print(lcm(N, M))
    #print("Yes" if N<=500*M else "No")
    #print(S.count("ABC"))


if __name__ == "__main__":
    main()
