import sys
input = sys.stdin.buffer.readline
#from itertools import permutations

def gcd(a: int, b: int):
    while b: a, b = b, a%b
    return a

def lcm(a: int, b: int):
    return a * b // gcd(a, b)


def main():
    N = int(input())
    mT = [tuple(input().decode().split()) for _ in [0,]*N]
    #N,M = map(int, input().split())
    X = input().decode().rstrip()

    p = 0
    res = 0
    for s,t in mT:
        nt = int(t)
        if p:
            res += nt
        if s==X:
            p = 1

    print(res)
    #vP = tuple(map(int, input().split()))
    #vA = set(map(int, input().split()))
    
    #print(lcm(N,M))
    #print(l, file=sys.stderr)
    #print("Yes" if X<=500*K else "No")
    #print(S.count("ABC"))


if __name__ == "__main__":
    main()
