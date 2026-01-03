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

from itertools import accumulate

n,w = li()
wv = []
for _ in range(n):
    wv.append(tuple(li()))
    
w0 = wv[0][0]
dic = {w0+i: [] for i in range(4)}
for k,v in wv:
    dic[k].append(v)
    
for wi in range(w0,w0+4):
    dic[wi] = [0] + sorted(dic[wi], reverse=True)
    dic[wi] = list(accumulate(dic[wi]))
    
ans = 0
for idx1, w1 in enumerate(dic[w0]):
    
    for idx2, w2 in enumerate(dic[w0+1]):
        
        for idx3, w3 in enumerate(dic[w0+2]):
            
            for idx4, w4 in enumerate(dic[w0+3]):
                
                if w0*idx1 + (w0+1)*idx2 + (w0+2)*idx3 + (w0+3)*idx4 > w:
                    continue
                
                ans = max(ans, w1+w2+w3+w4)
        
print(ans)