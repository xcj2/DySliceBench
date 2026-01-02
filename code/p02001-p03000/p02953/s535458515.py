#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str

def existFalse(decr):
    for i in range(len(decr)):
        if i == False:
            return True
    return False

def checkNonDecr(H):
    for i in range(len(H) - 1):
        if H[i] > H[i+1]:
            return False
    return True

def solve(N: int, H: "List[int]"):
    decr = [False] * N
    isGood = False
    while existFalse(decr):
        changed = False
        for i in range(N-1):
            if H[i] > H[i+1]:
                if decr[i] == False:
                    H[i] -= 1
                    decr[i] = True
                    changed = True
        isGood = checkNonDecr(H)
        if isGood: 
            break
        if changed == False:
            break
    if isGood:
        print(YES)
    else:
        print(NO)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    H = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, H)

if __name__ == '__main__':
    main()
