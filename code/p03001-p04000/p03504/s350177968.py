import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

from itertools import accumulate

n,ch = li()
MAX_T = 10**5+1

program = [[0]*MAX_T for _ in range(ch)]

endset = [set() for _ in range(ch)]
stc = []

for _ in range(n):
    s,t,c = li()
    c -= 1
    
    stc.append((s,t,c))
    endset[c].add(t)
    
stc.sort(key=lambda x:x[0])
    
for s,t,c in stc:
    if s in endset[c]:
        program[c][s] += 1
        program[c][t] -= 1
    else:
        program[c][s-1] += 1
        program[c][t] -= 1
    
for ci in range(ch):
    program[ci] = list(accumulate(program[ci]))
    
print(max([sum(time_span) for time_span in zip(*program)]))
