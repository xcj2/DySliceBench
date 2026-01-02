import collections
import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N = ii()

    memo = collections.defaultdict(lambda: 0)
    for i in range(N):
        S = list(input())
        S.sort()
        memo["".join(S)] += 1
    
    ans = 0
    for _,count in memo.items():
        ans += count * (count-1) // 2

    print(ans)
        


if __name__ == "__main__":
    main()