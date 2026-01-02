'''


■考え方
以下を繰り返し、白マスがなくなった時点のカウンターが答え。
1.黒マスに隣接する白マスを黒マスに塗り替える
2.カウンターに+1する

1詳細
1-0.現在の黒マスを全てキューへ入れる
1-1.キューから取り出し、隣接マスを「黒に塗り、キューへ入れる」
1-2. 1-1を繰り返し


'''
## import
from collections import deque # キュー、スタックに利用
# import itertools
# import math # 数学的計算に利用
# import numpy as np # 行列計算などに利用
import sys

## 初期設定
# input = sys.stdin.readline
def input():
    return sys.stdin.readline().rstrip()


sys.setrecursionlimit(10**7) # 再帰関数の呼び出し上限を増やす
inf = float('inf')

is_debug = True


black_str = '#'
white_str = '.'

def paint(q,M,h,w):
    '''
    キューから黒マスの位置を取り出し、隣接マスを「黒に塗り、キューへ入れる」
    '''
    out_q = deque()
    # 探索時の移動方向（上右下左） # delta y, delta x
    deltas = [[-1,0], [0,1], [1,0], [0,-1]]
    
    while len(q) > 0:
        # 探索する頂点uを取り出し
        y, x = q.popleft()

        ## uに隣接する全ての頂点について、白い場合は黒く塗り、out_qへ追加
        for delta in deltas:
            # 移動後の位置を算出
            after_y = y+delta[0]
            after_x = x+delta[1]
            # h,wの範囲に収まっていなければスキップ
            if after_y < 0 or after_y > h-1 or after_x < 0 or after_x > w-1:
                continue

            if M[after_y][after_x] == white_str:
                M[after_y][after_x] = black_str
                # out_qに追加
                out_q.append([after_y,after_x]) # キューに追加
    
    return out_q


def main():
    '''メイン処理'''

    ## input
    h, w = map(int, input().split())
    M = [list(input().rstrip()) for _ in range(h)]

    ans = 0
    # 塗るマスの位置を保持するキューを初期化
    q = deque()

    while True:
        ## 全てのマスが黒になったら終了
        # 以下の処理を入れると遅そうなのでコメントアウト
        # if white_str not in list(itertools.chain.from_iterable(M)):
        #     break

        # 各ターンで塗るマス。1=blackに塗るマス
        # paint_M = [[0]*w for _ in range(h)

        # 初回の場合、現在の黒マスを全てキューへ入れる
        if ans == 0:
            for i in range(h):
                for j in range(w):
                    if M[i][j] == black_str:
                        q.append([i,j])
        
        # キューから取り出し、隣接マスを「黒に塗り、キューへ入れる」
        q = paint(q,M,h,w)
        # 全てのマスが黒になったら終了
        if len(q) == 0:
            break

        ans += 1

    print(ans)


if __name__ == "__main__":
    # ファイル実行時に、main()関数を実行
    main()
