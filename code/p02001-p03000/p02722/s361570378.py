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
        n = iin()
        ans = set()
        ans.add(n)
        def check1(x):
            n1 = x-1
            i = 1
            while i*i<=n1:
                if n1%i==0:
                    ans.add(i)
                    ans.add(n1//i)
                i+=1
        def check2(x):
            n1 = n
            while n1%x==0:
                n1//=x
            n1 = n1%x
            if n1==1 :
                ans.add(x) 
        check1(n)
        i = 2
        while i*i<=n:
            if n%i==0:
                check2(i)
                if i!=n//i:
                    check2(n//i)
            i+=1
        ans = [i for i in ans if i>1]
        print(len(ans))
        # print(ans)






 
 
 
 
main()
 
# threading.Thread(target=main).start()