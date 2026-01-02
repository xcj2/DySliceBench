from random import randint
import sys
input = sys.stdin.readline
INF = 9223372036854775808


def calc_score(D, C, S, T):
    """
    開催日程Tを受け取ってそこまでのスコアを返す
    """
    score = 0
    last = [0]*26  # コンテストiを前回開催した日
    for d, t in enumerate(T, start=1):
        last[t-1] = d
        for i in range(26):
            score -= (d - last[i]) * C[i]
        score += S[d-1][t-1]
    return score


def update_score(D, C, S, T, score, ct, ci):
    """
    ct日目のコンテストをコンテストciに変更する
    スコアを差分更新する

    ct: change t 変更日 1-indexed
    ci: change i 変更コンテスト 1-indexed
    """
    last = [0]*26  # コンテストiを前回開催した日
    for d in range(1, ct):
        last[T[d-1]-1] = d
    prei = T[ct-1]  # 変更前に開催する予定だったコンテストi
    score -= S[ct-1][prei-1]
    score += S[ct-1][ci-1]
    for d in range(ct, D+1):
        if d != ct and T[d-1] == prei:
            break
        score += C[prei-1]*(d - ct)
        score -= C[prei-1]*(d - last[prei-1])
    for d in range(ct, D+1):
        if d != ct and T[d-1] == ci:
            break
        score += C[ci-1]*(d - last[ci-1])
        score -= C[ci-1]*(d - ct)
    T[ct-1] = ci
    return score, T


def local_search():
    pass


def main(D, C, S):
    T = []
    for d in range(D):
        # d日目終了時点で満足度が一番高くなるようなコンテストiを開催する
        max_score = -INF
        best_i = 1
        for i in range(26):
            T.append(i)
            score = calc_score(D, C, S, T)
            if max_score < score:
                max_score = score
                best_i = i
            T.pop()
        T.append(best_i)
    return T


if __name__ == '__main__':
    D = int(input())
    C = [int(i) for i in input().split()]
    S = [[int(i) for i in input().split()] for j in range(D)]
    T = [int(input()) for i in range(D)]
    M = int(input())
    DQ = [[int(i) for i in input().split()] for j in range(M)]
    score = calc_score(D, C, S, T)
    for d, q in DQ:
        score, T = update_score(D, C, S, T, score, d, q)
        print(score)
