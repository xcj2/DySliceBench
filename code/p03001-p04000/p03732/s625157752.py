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

from itertools import accumulate

n,w = li()
wi,vi = li()
w0 = wi
v_list = [[] for _ in range(4)]
v_list[0].append(vi)

for _ in range(n-1):
    wi,vi = li()
    v_list[wi-w0].append(vi)
    
for i in range(4):
    v_list[i].sort(reverse=True)
    v_list[i] = list(accumulate([0] + v_list[i]))
    
ans = 0
res = w
for w1 in range(len(v_list[0])):
    
    if w - w0*(w1) < 0:
        pass
    else:
        res1 = w - w0*(w1)
        ans1 = v_list[0][w1]
        ans = max(ans, ans1)
    

    for w2 in range(len(v_list[1])):

        if res1 - (w0+1)*(w2) < 0:
            pass
        
        else:
            res2 = res1 - (w0+1)*(w2)
            ans2 = ans1 + v_list[1][w2]
            ans = max(ans, ans2)

        
        
        for w3 in range(len(v_list[2])):
            
            if res2 - (w0+2)*(w3) < 0:
                pass
            
            else:
                res3 = res2 - (w0+2)*(w3)
                ans3 = ans2 + v_list[2][w3]
                ans = max(ans, ans3)
                
            
            for w4 in range(len(v_list[3])):

                if res3 - (w0+3)*(w4) < 0:
                    pass
                
                else:
                    res4 = res3 - (w0+3)*(w4)
                    ans4 = ans3 + v_list[3][w4]
                    ans = max(ans, ans4)

                
print(ans)