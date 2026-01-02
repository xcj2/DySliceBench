#! /usr/bin/env python3
import sys
sys.setrecursionlimit(10**9)


INF=10**20
def solve(S: str):
    if S == "RRR":  
        print(3)
    elif S[1:3] == "RR" or S[0:2] == "RR":
        print(2)
    else:
        ans = 0
        for s in S:
            if s == "R":
                ans = 1
        print(ans)
 
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)



if __name__ == "__main__":
    main()
