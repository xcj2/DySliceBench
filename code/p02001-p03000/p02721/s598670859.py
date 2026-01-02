import sys
sys.setrecursionlimit(10**8)
INF = float("inf")
 
 
def solve(N: int, K: int, C: int, S: str):
 
    L = []
    c = 0
    for i, d in enumerate(S):
        if d == "o" and c == 0:
            L.append(i)
            c = C
        elif c > 0:
            c -= 1
    R = []
    c = 0
    for i, d in enumerate(S[::-1]):
        if d == "o" and c == 0:
            R.append(N-i-1)
            c = C
        elif c > 0:
            c -= 1
 
    if len(L) != K:
        print()
        return
    for l, r in zip(L, R[::-1]):
        if l == r:
            print(l+1)
    return
 
 
def main():
 
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, K, C, S)
 
 
if __name__ == '__main__':
    main()