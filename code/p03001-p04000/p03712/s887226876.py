import sys
stdin = sys.stdin

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

h,w = li()
s = []
s.append(["#"]*(w+2))
for _ in range(h):
    temp = ["#"]
    temp = temp + lc()
    temp = temp + ["#"]
    s.append(temp)
              
s.append(["#"]*(w+2))
          
for si in s:
    print("".join(si))