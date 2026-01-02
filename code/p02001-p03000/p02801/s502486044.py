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
    #N,M = map(int, input().split())
    #vP = tuple(map(int, input().split()))
    #vA = set(map(int, input().split()))
    #vA = list(range(1,N+1))

    #print(l, file=sys.stderr)
    #l //= 2
    S = input().rstrip()
    #print(S)
    print(chr(ord(S)+1))
    #print(lcm(N, M))
    #print("Yes" if N<=500*M else "No")
    #print(S.count("ABC"))


if __name__ == "__main__":
    main()
