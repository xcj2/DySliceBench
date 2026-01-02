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

n,h = li()

def extract_gt_maxa(b: list, maxa: int) -> list:
    b.sort(reverse=True)
    ret = []
    for bi in b:
        if bi < maxa:
            break
        
        ret.append(bi)
        
    return ret

alist = []
blist = []
for _ in range(n):
    a,b = li()
    alist.append(a)
    blist.append(b)
    
b_gt_maxa = extract_gt_maxa(blist, max(alist))

ans = 0
for bi in b_gt_maxa:
    if h <= 0:
        break
    
    h -= bi
    ans += 1
    
if h > 0:
    ans += -(-h // max(alist))

print(ans)