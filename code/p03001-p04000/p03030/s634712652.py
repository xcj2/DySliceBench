import sys, math, collections, heapq, itertools
F = sys.stdin
def single_input(): return F.readline().strip("\n")
def line_input(): return F.readline().strip("\n").split()
def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while a % b > 0: a, b = b, a % b
    return b
  
def solve():
    N = int(single_input())
    point = dict()
    city = []
    for i in range(N):
        s, p = map(str, line_input())
        if s in point:
            point[s].append((int(p), i+1))
        else:
            point[s] = [(int(p), i+1)]
            city.append(s)
    city.sort()
    for s in city:
        l = point[s]
        l.sort(reverse = True)
        for p, i in l:
            print(i)
    return 0
  
if __name__ == "__main__":
    solve()