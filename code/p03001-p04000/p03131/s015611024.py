"""
NTC here
"""
import sys
inp= sys.stdin.readline
input = lambda : inp().strip()
flush= sys.stdout.flush
# import threading
# setrecursionlimit(10**6)
# threading.stack_size(2**26)

def iin(): return int(input())
def lin(): return list(map(int, input().split()))

# range = xrange
# input = raw_input

def main():
    k, a, b = lin()
    ans = 1
    lf = max(0, k - a+1)
    lf1 = lf//2
    if lf:
        ans = a+lf1*(b - a) + lf%2
    else:
        ans += k
    print(max(ans, k+1))








        
main()
#threading.Thread(target=main).start()