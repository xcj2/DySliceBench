import sys, math, collections, heapq, itertools
F = sys.stdin
def single_input(): return F.readline().strip("\n")
def line_input(): return F.readline().strip("\n").split()
def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while a % b > 0:
        a, b = b, a % b
    return b
  
def solve():
    N = int(single_input())
    ab = 0
    startB, endA, both = set(), set(), set()
    for i in range(N):
        s = str(single_input())
        for j in range(len(s) - 1):
            if s[j:j+2] == "AB": ab += 1
        if s[0] == "B" and s[-1] == "A": both |= {i}
        elif s[0] == "B": startB |= {i}
        elif s[-1] == "A": endA |= {i}

        
    ab += max(len(both) - 1, 0)
    if len(startB) == 0 and len(endA) == 0: print(ab)
    else:
        single = min(len(startB), len(endA))
        if len(both) > 0: single += 1
        ab += single
        print(ab)
    
    return 0
  
if __name__ == "__main__":
    solve()