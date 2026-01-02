"""
NTC here
"""
import sys
inp= sys.stdin.readline
input = lambda : inp().strip()
flush= sys.stdout.flush
# import threading
# sys.setrecursionlimit(10**6)
# threading.stack_size(2**25)

def iin(): return int(input())
def lin(): return list(map(int, input().split()))

# range = xrange
# input = raw_input


def main():
    from bisect import bisect as br
    n, d, A= lin()
    a = [lin() for i in range(n)]
    a.sort()
    a+= [[10**9+1+2*d,0]]
    a1=[i for i, j in a ]
    a2 = [0]*(n+1)
    ch = 0
    ans = 0
    for i in range(n):
        ch -= a2[i]
        x = a[i][1]-A*ch
        if x>0:    
            pos = a[i][0]
            r = br(a1, pos+2*d)
            amt = (x+A-1)//A
            a2[r]+=amt
            ch += amt
            ans += amt
    print(ans)





            
        

        
main()
# threading.Thread(target=main).start()
