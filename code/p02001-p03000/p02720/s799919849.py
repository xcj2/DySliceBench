"""
NTC here
"""
import sys
inp = sys.stdin.readline
def input(): return inp().strip()
# flush= sys.stdout.flush
# import threading
# sys.setrecursionlimit(10**6)
# threading.stack_size(2**26)
 
def iin(): return int(input())
 
 
def lin(): return list(map(int, input().split()))
 
 
# range = xrange
# input = raw_input
 
def main():
    T = 1
    while T:
        T-=1
        k = iin()
        ans = [[0 for i in range(10)] for j in range(10)]
        for i in range(10):
            ans[0][i]=1
        for i in range(1, 10):
            for j in range(10):
                sm = ans[i-1][j]
                if j-1>=0:
                    sm+=ans[i-1][j-1]
                if j+1<10:
                    sm+=ans[i-1][j+1]
                ans[i][j] = sm
        # print(*ans, sep = '\n')
        br = 0
        i1, j1 = 0, 1
        for i in range(10):
            if br:break
            for j in range(1, 10):
                # print(i, j, k)
                if k<=ans[i][j]:
                    i1, j1 = i, j
                    br = 1
                    break
                else:
                    k-=ans[i][j]
        # print(i1, j1)
        sol = [str(j1)]
        for i in range(i1-1, -1, -1):
            chk = ([j1-1] if j1-1>=0 else []) + [j1] + ([j1+1] if j1+1<10 else [])
            for j in chk:
                if k<=ans[i][j]:
                    sol.append(str(j))
                    j1 = j
                    break
                else:
                    k-=ans[i][j]
        print(''.join(sol))





 
 
 
 
main()
 
# threading.Thread(target=main).start()