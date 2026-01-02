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
        n, m = lin()
        a = lin()
        sm = sum(a)
        ch = 0
        lst = sm/(4*m)
        for i in a:
            if i>=lst:
                ch+=1
        print('Yes' if ch>=m else 'No')

 
 
 
 
 
main()
 
# threading.Thread(target=main).start()