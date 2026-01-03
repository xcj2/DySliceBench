import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    def main():
        S=str(input())

        # bit全探索
        # https://qiita.com/gogotealove/items/11f9e83218926211083a#%E4%BE%8B%E9%A1%8C-1
        n = len(S)-1
        if n==0:
            return int(S)
        else:
            # 昇順での探索だよ
            ans=0
            for i in range(2 ** n):
                temp = n+1
                for j in range(n):  # このループが一番のポイント
                    if ((i >> j) & 1):
                        ans+=int(S[-j-1:temp])
                        temp=-j-1
                    if j==n-1:
                        ans+=int(S[:temp])# 順
            return ans# に右にシフトさせ最下位bitのチェックを行う
    print(main())


resolve()