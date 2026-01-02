#!/usr/bin/env python3
import sys
import itertools

def solve(S: str):
    N = len(S) 
    answer = [0]*N
    R_count = 0
    for i in range(N):
        if S[i]== "L":
            answer[i]+= R_count//2
            answer[i-1]+=(R_count+1)//2
            R_count = 0
        else:
            R_count+=1
    
    L_count = 0
    for i in range(N-1,-1,-1):
        if S[i]=="R":
            answer[i]+=L_count//2
            answer[i+1]+=(L_count+1)//2
            L_count=0
        else:
            L_count+=1
    
    print(*answer)

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)

if __name__ == '__main__':
    main()
