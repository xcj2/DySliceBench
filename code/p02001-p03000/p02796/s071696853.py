import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n = I()
    span = [None for _ in range(n)]
    for i in range(n):
        x, l = LI()
        span[i] = [x-l, x+l]
    span.sort(key=lambda x: x[1])
    choice = [[-float("inf"),-float("inf")]]
    for each_span in span:
        if choice[-1][1] <= each_span[0]:
            choice.append(each_span)
    
    ans = len(choice)-1
    print(ans)
main()
