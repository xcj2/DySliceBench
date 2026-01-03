import sys
stdin = sys.stdin

def li(): return [int(x) for x in stdin.readline().split()]
def li_(): return [int(x)-1 for x in stdin.readline().split()]
def lf(): return [float(x) for x in stdin.readline().split()]
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(ns())
def nf(): return float(ns())

s = lc()

if (("N" in s) and (not "S" in s)) or (("S" in s) and (not "N" in s)):
    print("No")
elif (("W" in s) and (not "E" in s)) or (("E" in s) and (not "W" in s)):
    print("No")
else:
    print("Yes")