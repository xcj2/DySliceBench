
import numpy as np
from functools import *

import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline


def acinput():
    return list(map(int, input().split(" ")))


def factorial(n):
    fact = 1
    for integer in range(1, n + 1):
        fact *= integer
    return fact


H, W, NN = acinput()

initp = np.array(acinput())

S = list(input())[:-1]
T = list(input())[:-1]
#S = list(input().split(""))
#T = list(input().split(""))


def position_relative(direction, direction_op, cs, flg, seq1, seq2, N):
    global H, W
    # N=len(seq1)
    for i in range(len(seq1)):
        s1 = seq1[i]
        s2 = seq2[i]

        #print(cs,flg)
        if s1 == direction:
            cs += flg

        if flg > 0:
            if cs > N:
                return False

        else:
            if cs <= 0:
                return False
            # elif cs>N:
            #    cs=N
        #print(cs)
        if s2 == direction_op:
            #print("op",N)
            cs -= flg
    
    
        if cs > N:
           cs = N
        
        if cs <= 0:
            cs = 1

    return cs


sr = position_relative("R", "L", initp[1], 1, S, T, W)
sl = position_relative("L", "R", initp[1], -1, S, T, W)
su = position_relative("U", "D", initp[0], -1, S, T, H)
sd = position_relative("D", "U", initp[0], 1, S, T, H)

#print(sr, sl, su, sd)

# su=0
# if sr or sl or su or sd:
if sr*sl*su*sd == 0:
    print("NO")
else:
    print("YES")
