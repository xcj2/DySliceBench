import sys, collections
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**10
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    n = I()
    st = [LI() for _ in range(n)]
    # 開始時間が大丈夫で、終了時間の早いものから入れていく
    st.sort(key= lambda x: x[1])

    ans = 0
    end_time = 0
    for i in range(n):
        if st[i][0] > end_time:
            ans += 1
            end_time = st[i][1]

    print(ans)

if __name__ == '__main__':
    resolve()

