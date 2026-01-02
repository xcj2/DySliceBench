import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    d, g = LI()
    lst = [0 for _ in range(d)]
    for i in range(d):
        p, c = LI()
        lst[i] = (p, c)
    
    ans = float("inf")
    bits = itertools.product([0,1],repeat=d)

    for bit in bits:
        point = 0
        cnt = 0
        for i in range(d):
            if bit[i] == 1:
                cnt += lst[i][0]
                point += (i+1)*100*lst[i][0] + lst[i][1]
        for i in range(d-1,-1,-1):
            if point>=g:
                break
            if bit[i] == 0:
                for _ in range(lst[i][0]-1):
                    cnt += 1
                    point += (i+1)*100
                    if point>=g:
                        break
        if point>=g:
            ans = min(ans,cnt)
    print(ans)

main()            
