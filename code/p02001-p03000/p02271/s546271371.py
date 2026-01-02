import sys
import collections

# Set max recursion limit
sys.setrecursionlimit(1000000)


def li_input():
    return [int(_) for _ in input().split()]

def to_bin(k):
    return bin(k)[2:]


def main():
    N = int(input())
    A = li_input()
    M = int(input())
    Q = li_input()

    B = []
    D = collections.defaultdict(lambda: 0)

    for i in range(2 ** len(A)):
        b = to_bin(i)

        if len(b) < len(A):
            b = "0" * (len(A) - len(b)) + b
        
        B.append(b)

    for b in B:
        s = 0
        for i,is_add in enumerate(b):
            if is_add == "1":
                s += A[i]

        D[s] = 1
    
    for q in Q:
        if D[q] == 1:
            print("yes")
        else:
            print("no")
            


main()

