"""
NTC here
"""
import sys
inp = sys.stdin.readline


def input(): return inp().strip()


flush = sys.stdout.flush
# import threading
# sys.setrecursionlimit(10**6)
# threading.stack_size(2**25)


def iin(): return int(input())


def lin(): return list(map(int, input().split()))

# range = xrange
# input = raw_input


def main():
    def fn(n):
        if n<0:return 0
        return (n*(n+1))//2
    n = iin()
    a = lin()
    dc = {}
    for i in a:
        try:
            dc[i]+=1
        except:
            dc[i] = 1
    sm = 0
    for i in dc:
        sm+= fn(dc[i]-1)
    for i in a:
        x = dc[i]
        ch = sm - fn(x-1) + fn(x-2)
        print(ch)

main()
# threading.Thread(target=main).start()
