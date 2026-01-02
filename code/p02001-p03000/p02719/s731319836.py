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
        n, k = lin()
        n = n%k
        ans = n
        done = set()
        while n not in done:
            n = abs(n-k)
            ans = min(n, ans)
            done.add(n)
        print(ans)


 
 
 
 
 
main()
 
# threading.Thread(target=main).start()