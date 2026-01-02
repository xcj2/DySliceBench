"""
NTC here
"""
import sys
input= sys.stdin.readline
# import t  hreading
# setrecursionlimit(10**6)
# threading.stack_size(2**26)

def iin(): return int(input())
def lin(): return list(map(int, input().split()))

# range = xrange
# input = raw_input

def main():
    n=iin()
    h=lin()
    ans=[0]*(n-2)+[abs(h[-2]-h[-1]),0]
    for i in range(n-3,-1,-1):
        ans[i]=min(
            abs(h[i]-h[i+1])+ans[i+1],
            abs(h[i]-h[i+2])+ans[i+2]
            )
    print(ans[0])
        



                









        
main()
#threading.Thread(target=main).start()
