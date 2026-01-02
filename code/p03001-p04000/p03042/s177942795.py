import sys, math, collections, heapq, itertools
F = sys.stdin
def single_input(): return F.readline().strip("\n")
def line_input(): return F.readline().strip("\n").split()
def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while a % b > 0: a, b = b, a % b
    return b
  
def solve():
    S = single_input()
    YYMM = False
    MMYY = False
    if 1 <= int(S[2:]) <= 12: YYMM = True
    if 1 <= int(S[:2]) <= 12: MMYY = True

    if YYMM and MMYY: print("AMBIGUOUS")
    elif YYMM: print("YYMM")
    elif MMYY: print("MMYY")
    else: print("NA")
    return 0
  
if __name__ == "__main__":
    solve()