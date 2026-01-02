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
    n, k= lin()
    h=lin()
    ans=[0]*(n)
    for i in range(n-2,-1,-1):
        ans[i]=min(
            [abs(h[i]-h[j+i+1])+ans[i+j+1] for j in range(min(n-i-1,k))]
            )
    print(ans[0])
        



                









        
main()
#threading.Thread(target=main).start()
