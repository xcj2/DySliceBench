#!/usr/bin/env python3
import sys


def solve(N: int, M: int, P: "List[int]", Y: "List[int]"):
    hashTable = {}

    for i in range(M):
        if hashTable.get(P[i]) == None:
            hashTable[P[i]] = [Y[i]]
        else:
            hashTable[P[i]].append(Y[i])
    
    # Year: idnumber
    answerTable = {}

    for key,value in hashTable.items():
        value.sort()
        
        for i,v in enumerate(value):
            answerTable[v] = str(key).zfill(6) + str(i+1).zfill(6)
    
    for i in range(M):
        print(answerTable[Y[i]])

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    P = [int()] * (M)  # type: "List[int]"
    Y = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        P[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    solve(N, M, P, Y)

if __name__ == '__main__':
    main()
