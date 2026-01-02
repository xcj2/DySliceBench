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

n = ni()
t,a = li()
h = list(li())

temp_list = []

for i in range(n):
    temp_list.append(t - h[i]*0.006)
 
ans = 10**18
for j, temp in enumerate(temp_list):
    if abs(a-temp) < ans:
        point = j
        ans = abs(a-temp)
        
print(point+1)