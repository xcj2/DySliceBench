#!/usr/bin/env python3
import sys


def solve(N: int, S: str):
    R = [0]*N
    G = [0]*N
    B = [0]*N
    for i in range(N-1,-1,-1):
        if S[i] == "R":
            if i == N-1:
                R[i] = 1
            else:
                R[i] = R[i+1] + 1 
                G[i] = G[i+1]
                B[i] = B[i+1]
        elif S[i] == "G":
            if i == N-1:
                G[i] = 1
            else:
                R[i] = R[i+1] 
                G[i] = G[i+1] + 1
                B[i] = B[i+1]
        elif S[i] == "B":
            if i == N-1:
                B[i] = 1
            else:
                R[i] = R[i+1] 
                G[i] = G[i+1]
                B[i] = B[i+1]+1

    answer = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            if S[i] == "R":
                if S[j] == "G":
                    answer += B[j+1]
                    if 2*j-i < N and S[2*j-i] == "B":
                        answer -= 1
                elif S[j] == "B":
                    answer += G[j+1]
                    if 2*j-i < N and S[2*j-i] == "G":
                        answer -= 1
            elif S[i] == "G":
                if S[j] == "R":
                    answer += B[j+1]
                    if 2*j-i < N and S[2*j-i] == "B":
                        answer -= 1
                elif S[j] == "B":
                    answer += R[j+1]
                    if 2*j-i < N and S[2*j-i] == "R":
                        answer -= 1
            elif S[i] == "B":
                if S[j] == "G":
                    answer += R[j+1]
                    if 2*j-i < N and S[2*j-i] == "R":
                        answer -= 1
                elif S[j] == "R":
                    answer += G[j+1]
                    if 2*j-i < N and S[2*j-i] == "G":
                        answer -= 1

    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)

if __name__ == '__main__':
    main()
