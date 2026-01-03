import sys
from collections import Counter
def I(): return int(sys.stdin.readline().rstrip())
def IL(): return map(int,sys.stdin.readline().rstrip().split())

def Main():
    n = I()
    l = list(IL())
    a = Counter(l)
    f = s = 0
    l = list(set(l))
    l.sort(reverse=True)
    for rep in l:
        if 4<=a[rep]:
            f = max(f,rep)
            s = max(s,rep)
            break
        elif 2<=a[rep]:
            if f==0:
                f = rep
            else:
                s = rep
                break
    
    print(f*s)
    return

if __name__=='__main__':
    Main()