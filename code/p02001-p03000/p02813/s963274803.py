import sys
input = sys.stdin.readline
from itertools import permutations

def gcd(a: int, b: int):
    """ https://cocodrips.hateblo.jp/entry/2014/03/05/143623
    """
    while b:
        a, b = b, a%b
    return a

def lcm(a: int, b: int):
    return a * b // gcd(a, b)


def main():
    N = int(input())
    #K,X = map(int, input().split())
    vP = tuple(map(int, input().split()))
    vQ = tuple(map(int, input().split()))
    vA = list(range(1,N+1))

    p,q = 0,0
    for i,vI in enumerate(permutations(vA)):
        #print(i,vI)
        #if i==7: break
        if vI==vP:
            p = i
        if vI==vQ:
            q = i
    print(abs(p-q))
    #S = input().rstrip()
    #print(S)
    #print(lcm(N, M))
    #print("Yes" if X<=500*K else "No")
    #print(S.count("ABC"))


if __name__ == "__main__":
    main()
