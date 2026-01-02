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

c = []
for _ in range(3):
    c.append(list(li()))
    
correct = True
a1 = 0
a2 = c[1][0] - c[0][0]
a3 = c[2][0] - c[0][0]
b1 = c[0][0]
b2 = c[0][1]
b3 = c[0][2]

a = [a1,a2,a3]
b = [b1,b2,b3]

for i in range(3):
    for j in range(3):
        if a[i] + b[j] != c[i][j]:
            correct = False
            
print("Yes") if correct else print("No")