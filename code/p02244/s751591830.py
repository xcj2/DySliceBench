# import bisect
# from collections import Counter, deque
# import copy
# from fractions import gcd

def resolve():
    N = 8

    # すでに配置されたクイーンの効きが及ばない位置であればTrueを返す
    def check(row, FR):
        # まず横の効きで取られないかチェックする
        # すでにクイーンの配置された行だとダメ
        if row in FR:
            return False

        # 次に斜めの効きで取られないかチェックする
        # enumerate関数により、リストFRの添字fc(filled_column)と要素fr(filled_row)を取得
        for fc, fr in enumerate(FR):
            # distだけ離れた列fcが着目されている
            dist = len(FR) - fc
            # 左上あるいは左下にクイーンがあったらアウト
            if (row == fr - dist) or \
                    (row == fr + dist):
                return False
        return True

    # クイーンの可能な配置をすべてprintする関数
    def search(FR):
        # FRはFilled Rowsの略。
        # 第column列のFR[column]行目にすでにクイーンが配置済みであることを意味する。

        # すべての列に配置でき次第出力。クイーンのある位置を黒く塗りつぶす
        if len(FR) == N:
            for i in range(M):
                if FR[X[i]] != Y[i]:
                    break
                elif i==M-1:
                    for k in range(N):
                        for j in range(N):
                            print('Q' if FR[k] == j else '.', end='')
                        print()
                    return

        # クイーンを配置した行数を格納するリストFRを作成
        for row in range(N):
            if check(row, FR):
                FR.append(row)
                # 再帰的に探索する。「以下同様」という意味。
                search(FR)
                # どの行に入れても無理だと判明したら、
                # 最後の行をpopし、もう１回ループを回して別の行でいけないかと模索する
                FR.pop()


    M=int(input())
    X,Y = [0] * M, [0] * M
    for i in range(M):
        X[i], Y[i] = map(int, input().split())

    search([])


resolve()
