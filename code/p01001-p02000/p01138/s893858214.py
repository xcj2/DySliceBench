import sys, collections
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**10
MOD = 1000000007
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def resolve():
    
    def hhmmss_to_s(t):
        hh = int(t[0:2])
        mm = int(t[3:5])
        ss = int(t[6:8])
        return hh*3600+mm*60+ss

    while True:
        n = I()
        if n==0:
            break
        else:
            cnt = [0]*(24*3600+1)
            for _ in range(n):
                leave, arrive = map(hhmmss_to_s, input().split())
                cnt[leave] += 1
                cnt[arrive] -= 1
            for i in range(24*3600):
                cnt[i+1] += cnt[i]

            print(max(cnt))


if __name__ == '__main__':
    resolve()
