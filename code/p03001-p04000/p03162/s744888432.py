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
    n = iin()
    Q = [lin() for i in range(n)]
    ans = [[0, 0, 0] for i in range(n+1)] 
   # print(ans)
    for i in range(n-1, -1, -1):
        for j in range(3):
            ans[i][j]=Q[i][j]+max([
                ans[i+1][k] for k in range(3) if k!=j
            ])
  #  print(ans)
    print(max(ans[0]))

        



                









        
main()
#threading.Thread(target=main).start()
