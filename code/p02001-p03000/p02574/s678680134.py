import bisect
import sys
import math
input = sys.stdin.readline
import functools

from collections import defaultdict

############ ---- Input Functions ---- ############

def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

############ ---- Solution ---- ############


def gcd(a, b):
    if b > a:
        return gcd(b, a)
    m = a % b
    if m == 0:
        return b
    return gcd(b, m)

def solve():
    N = inp()
    AA = inlt()

    MAX = 10 ** 6 + 5
    freq = [0 for i in range(MAX)]
    cnt = [0 for i in range(MAX)]
    
    gcd_cum = AA[0]

    for i in range(N):
        freq[AA[i]] += 1
        gcd_cum = gcd(gcd_cum, AA[i])

    for i in range(2, MAX):
        for j in range(i, MAX, i):
            cnt[i] += freq[j]

    pairwise = True
    for i in range(2, MAX):
        if cnt[i] > 1:
            pairwise = False
            break
    
    if gcd_cum == 1 and pairwise:
        return "pairwise coprime"

    if gcd_cum == 1:
        return "setwise coprime"
    
    return "not coprime"
    

if len(sys.argv) > 1 and sys.argv[1].startswith("input"):
    f = open("./" + sys.argv[1], 'r')
    input = f.readline

res = solve()
print(str(res))
