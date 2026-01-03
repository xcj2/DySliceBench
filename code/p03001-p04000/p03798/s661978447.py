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

def nex_animal(prev: str, cur:str, say: str) -> str:
    ret_dic = {("S", "S", "o"): "S", ("S", "S", "x"): "W",
               ("S", "W", "o"): "W", ("S", "W", "x"): "S",
               ("W", "S", "o"): "W", ("W", "S", "x"): "S",
               ("W", "W", "o"): "S", ("W", "W", "x"): "W"}
    
    return ret_dic[(prev, cur, say)]

n = ni()
s = lc()
ans = [""]*n

init = {"o":[("S", "S", "S"), ("W","S","W"), ("W","W","S"), ("S","W","W")],
        "x":[("W", "S", "S"), ("S","S","W"), ("S","W","S"), ("W","W","W")]}

exist = False
if s[-1] == "o":
    for a1,a2,a3 in init["o"]:
        ans = [""]*n
        ans[-2], ans[-1], ans[0] = a1, a2, a3
        
        for i in range(n-1):
            if i < n-3:
                ans[i+1] = nex_animal(ans[i-1], ans[i], s[i])
            elif i == n-3:
                if ans[i+1] != nex_animal(ans[i-1], ans[i], s[i]):
                    break
                
            else:
                if ans[i+1] != nex_animal(ans[i-1], ans[i], s[i]):
                    break
                
                else:
                    print("".join(ans))
                    exist = True
                    break
                
        if exist:
            break
                
else:
    for a1,a2,a3 in init["x"]:
        ans = [""]*n
        ans[-2], ans[-1], ans[0] = a1, a2, a3
        
        for i in range(n-1):
            if i < n-3:
                ans[i+1] = nex_animal(ans[i-1], ans[i], s[i])
            
            elif i == n-3:
                if ans[i+1] != nex_animal(ans[i-1], ans[i], s[i]):
                    break
            
            else:
                if ans[i+1] != nex_animal(ans[i-1], ans[i], s[i]):
                    break
                
                else:
                    print("".join(ans))
                    exist = True
                    break
                
        if exist:
            break
    
                    
if not exist:
    print(-1)        