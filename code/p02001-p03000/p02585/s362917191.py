import math

def split_to_loops(G):
    # G[i]: i の次の頂点(0 <= i <= |G|-1) を格納しているリストがあるとき、
    # ループ単位にリストを分割する。
    # ex) G = [1, 3, 4, 0, 2]
    # => "0 -> 1 -> 3 -> 0" というループと
    #    "2 -> 4 -> 2" というループがある
    # このメソッドでは、[[0,1,3],[2,4]]が返される

    loops = []
    _all = set(range(len(G)))

    while _all:
        s = _all.pop()
        loop = [s]
        v = G[s]
        while v != s:
            _all.remove(v)
            loop.append(v)
            v = G[v]

        loops.append(loop)

    return loops

def find_max_continued(A, n):
    # A 内で連続した1個以上n個以内の領域の合計の最大値を見つける
    # ex) A = [-2, 4, 3, -1, 2, 6, 4, 5, -3], n = 3
    #       => [6, 4, 5] の合計 =15 が最大
    # ex) A = [-2, 4, 3, -1, 2, 6, -4, 5, -3], n = 3
    #       => [2, 6] の合計 =8 が最大
    # ex) A = [-2, 4, 3, -1, 2, 6, -4, 5, -3], n = 4
    #       => [3, -1, 2, 6] の合計 =10 が最大
    # ex) A = [-2, -4, -3, -1, -2, -6, -4, -5, -3], n = 3
    #       => [-1] の合計 =-1 が最大

    # n = 1のとき
    _max = max(A)

    # n = 2以上
    L = len(A)
    for d in range(2, min(n+1, L+1)):
        _sum = sum(A[:d])
        _max = max(_max, _sum)
        # 領域を右にずらしながら合計を計算することで、O(L) で計算できる 
        for i in range(d, L):
            _sum += A[i] - A[i-d]
            _max = max(_max, _sum)
        for i in range(d):
            _sum += A[i] - A[L-d+i]
            _max = max(_max, _sum)

    return _max

def find_max_in_one_loop(loop, K, C):
    # loopにおける1回以上K回以内の移動でのスコアの最大値を見つける
    L = len(loop)
    loop_c = [C[v] for v in loop] # ループに登場するマスのスコアのリスト

    # 一周したときのスコア
    sum_1_loop = sum(loop_c)
    # print(f'{loop_c=}, {sum_1_loop=}')

    if sum_1_loop < 0:
        # 一周したときに負になるようなら、ループしないほうがいい
        return find_max_continued(loop_c, min(K, L))
    else:
        # 一周以上移動できない場合
        if K < L:
            return find_max_continued(loop_c, K)

        # 一周以上移動できる場合
        # できるだけループしたほうがいい

        n_loops = K // L # ループできる回数

        # ただし、スコアが [1 1 1 -2] のようになっている場合、
        # 1周するより負の数を避けて途中で終了したほうがいいので、
        # 一旦わざとループできる回数から1周分減らしておく
        n_loops -= 1
        
        score = sum_1_loop * n_loops
        K -= n_loops * L # 残りの移動回数 (L <= K < 2*L)

        # 一周未満の時のスコアの最大値
        score_no_loop = find_max_continued(loop_c, L)
        # print(f'{K=}, {L=}, {n_loops=}, {score=}, {score_no_loop=}')
        # 一周してさらにK-L回以内で移動するときのスコア
        score_loop = sum_1_loop
        if K != L:
            # print(f'{K=}, {L=}, {K-L}, {find_max_continued(loop_c, K - L)}')
            score_loop += find_max_continued(loop_c, K - L)
        # 最後、一周しないほうがいいか、一周したほうがいいか、スコアの大きいほうを選ぶ
        score += max(score_no_loop, score_loop)
        return score

def main():
    N, K = map(int, input().split())
    # P は番号を1引くことで配列で扱いやすくする
    P = list(map(lambda x: int(x)-1, input().split()))
    C = list(map(int, input().split()))

    # ループごとに分割
    # ex) P = [1, 3, 4, 0, 2]
    # => "0 -> 1 -> 3 -> 0" というループと
    #    "2 -> 4 -> 2" というループがある
    # => loops = [[0,1,3],[2,4]]
    loops = split_to_loops(P)
    # print(f'{loops=}')

    ans = -(10 ** 10)
    for loop in loops:
        # [0,1,3] などのループ単位で、1回以上K回以内の移動での最大値を見つける
        # その最大値の中からさらに最大値を見つけて、答えとする
        ans = max(ans, find_max_in_one_loop(loop, K, C))
    
    print(ans)

if __name__ == '__main__':
    main()