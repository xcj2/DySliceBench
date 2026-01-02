from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(1000000)

# INF = float('inf')
INF = int(1e10)

def input():
    return stdin.readline()[:-1]

def is_kaibun(S):
    flag = True
    # print(S)
    for i in range((len(S) + 1) // 2):
        # print(i, S[i], S[len(S) - i - 1])
        if S[i] != S[len(S) - i - 1]:
            flag = False
            break
    return flag

def main():
    from builtins import int, map
    S = input()
    N = len(S)
    if is_kaibun(S) and is_kaibun(S[:N // 2]) and is_kaibun(S[N // 2 + 1:]):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()