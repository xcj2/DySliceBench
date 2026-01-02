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
    h, n = lin()
    a = [lin() for i in range(n)]
    ans = [-1]*(h+1)
    ans[0] = 0
    for i in range(1, h+1):
        ans[i] = min([
            ans[max(0, i-j)]+k for j, k in a
            ])
        
        
    print(ans[h])



            
        

        
main()
# threading.Thread(target=main).start()
