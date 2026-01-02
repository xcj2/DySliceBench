import sys
import itertools
from collections import defaultdict, deque
from copy import deepcopy
    
input = sys.stdin.readline
def RD(): return input().rstrip()
def F(): return float(input().rstrip())
def I(): return int(input().rstrip())
def MI(): return map(int, input().split())
def MF(): return map(float,input().split())
def LI(): return tuple(map(int, input().split()))
def LF(): return list(map(float,input().split()))
def Init(H, W, num): return [[num for i in range(W)] for j in range(H)]
    
    
def main():
    N = I()
    P = LI()
    Q = LI()
    index = 1
    seq = [i+1 for i in range(N)]
    for i in itertools.permutations(seq, r=None):
        if P == i:
            a = index
        if Q == i:
            b = index        
        index += 1
    print(abs(a-b))

if __name__ == "__main__":
    main()