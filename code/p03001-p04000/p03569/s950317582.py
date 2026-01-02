import sys
from heapq import heappop, heappush
#input = sys.stdin.readline

def inp(): # n=1
    return int(input())
def inpm(): # x=1,y=2
    return map(int,input().split())
def inpl(): # a=[1,2,3,4,5,...,n]
    return list(map(int, input().split()))
def inpls(): # a=['1','2','3',...,'n']
    return list(input().split())
def inplm(n): # x=[] 複数行
    return list(int(input()) for _ in range(n))
def inpll(n): # [[1,1,1,1],[2,2,2,2],[3,3,3,3]]
    return sorted([list(map(int, input().split())) for _ in range(n)])
def graphm():
    n=inp()
    g=[[] for _ in range(n)]
    for _ in range(n-1):
        a,b,w=inpm()
        a-=1
        b-=1
        g[a].append((b,w))
        g[b].append((a,w))
    return n,g


def main():
    s=input()
    n=len(s)
    i_l = 0
    i_r = n-1
    cnt = 0
    flag = False
    while True:
        if i_l >= i_r:
            if i_l == i_r:
                flag = True
            if flag:
                print(cnt)
                return
            else:
                print(-1)
                return
        if s[i_l] == s[i_r]:
            i_l += 1
            i_r -= 1
            flag = True
        elif s[i_l] == 'x' and s[i_r] != 'x':
            cnt += 1
            i_l +=1
            flag = False
        elif s[i_l] != 'x' and s[i_r] == 'x':
            cnt += 1
            i_r -=1
            flag = False
        elif s[i_l] != 'x' and s[i_r] != 'x' and s[i_l] != s[i_r]:
            print(-1)
            return

if __name__ == "__main__":
    main()
