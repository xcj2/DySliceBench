

"""
NTC here
"""
import sys
inp = sys.stdin.readline
def input(): return inp().strip()
flush= sys.stdout.flush
# import threading
# sys.setrecursionlimit(10**6)
# threading.stack_size(2**26)

def iin(): return int(input())


def lin(): return list(map(int, input().split()))

# out = []
# range = xrange
# input = raw_input

def main():
    n = iin()
    ans = (n*(n+1))//2
    for i in range(3, n+1, 3):ans-=i
    for i in range(5, n+1, 5):ans-=i
    for i in range(15, n+1, 15):ans+=i
    print(ans)

main()
# threading.Thread(target=main).start()
