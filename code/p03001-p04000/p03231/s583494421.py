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

def get_gcd(a:int, b:int) -> int:
    while b:
        a, b = b, a % b
    return a
    
def get_lcm(a:int, b:int) -> int:
    return (a // get_gcd(a,b)) * b

n,m = li()
s = lc()
t = lc()

sx = dict()
tx = dict()

lcm = get_lcm(n,m)

for idx, i in enumerate(range(1,lcm+1,lcm//n)):
    sx.update({i:s[idx]})

for idx, j in enumerate(range(1,lcm+1,lcm//m)):
    tx.update({j:t[idx]})
    
common_key = list(set(list(sx.keys())) & set(list(tx.keys())))

exist = True
for c in common_key:
    if sx[c] != tx[c]:
        exist = False
        break
    
if exist:
    print(lcm)
else:
    print(-1)