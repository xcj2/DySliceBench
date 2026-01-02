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

def judge(s:list) -> bool:
    
    if not s[0] == 'A':
        return False
        
    if not 'C' in s[2:-1]:
        return False
        
    s.remove('C')
    s.remove('A')
    
    for si in s:
        if not 'a' <= si <= 'z':
            return False
            
        
    return True


s = lc()

ac = judge(s)
print('AC') if ac else print('WA')