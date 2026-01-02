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
    dc=[2,0,0,0,0]
    no = 0
    for _ in range(3):
        a, b= lin()
        if a==b:
            no = 1
        dc[a]+=1
        dc[b]+=1
    print('YES' if max(dc)==2 and not no else 'NO')
    





        
main()
#threading.Thread(target=main).start()