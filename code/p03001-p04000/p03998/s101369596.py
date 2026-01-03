import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    sa = collections.deque(list(S()))
    sb = collections.deque(list(S()))
    sc = collections.deque(list(S()))
    ans = None 
    nxt = "a"

    while ans == None:
        if nxt == "a":
            if len(sa) == 0:
                ans = "A"
            else:
                nxt = sa.popleft()
        if nxt == "b":
            if len(sb) == 0:
                ans = "B"
            else:
                nxt = sb.popleft()
        if nxt == "c":
            if len(sc) == 0:
                ans = "C"
            else:
                nxt = sc.popleft()
    print(ans)
main()            
