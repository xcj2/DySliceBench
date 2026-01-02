import sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**10
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def resolve():
    while True:
        H = I()
        if H==0:
            break
        else:
            s = [LI() for _ in range(H)]

            score = 0
            while True:
                # 消滅判定
                score_tmp = 0
                for i in range(H):
                    prev = 0
                    cnt = 1
                    for j in range(5):
                        if s[i][j]==prev:
                            cnt += 1
                        else:
                            if cnt>=3:
                                score_tmp += prev*cnt
                                for k in range(cnt):
                                    s[i][j-cnt+k] = 0
                            prev = s[i][j]
                            cnt = 1
                    if cnt>=3:
                        score_tmp += prev*cnt
                        for k in range(cnt):
                            s[i][j+1-cnt+k] = 0
                # print('s')
                # for i in s:
                #     print(i)
                if score_tmp==0:
                    break
                score += score_tmp

                # 落下処理
                # その石がどれだけ落下するかの算出
                drop = [[0]*5 for _ in range(H)]
                for i in range(5):
                    for j in range(H-1):
                        drop[H-j-2][i] = drop[H-j-1][i] + (1 if s[H-j-1][i]==0 else 0)
                # print('drop')
                # for i in drop:
                #     print(i)
                
                # 落下先にコピー
                for i in range(5):
                    for j in range(H):
                        if drop[H-j-1][i]!=0:
                            s[H-j-1+drop[H-j-1][i]][i] = s[H-j-1][i]
                            s[H-j-1][i] = 0
                # print('dropped s')
                # for i in s:
                #     print(i)

            print(score)

if __name__ == '__main__':
    resolve()
