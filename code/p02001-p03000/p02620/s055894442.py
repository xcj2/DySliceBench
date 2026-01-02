from random import randint
import sys
input = sys.stdin.readline


def calc_score(D, C, S, T):
    """
    開催日程Tを受け取ってそこまでのスコアを返す
    """
    contest_last_opened = [0]*26  # コンテストiを前回開催した日
    score = 0
    for d, t in enumerate(T, start=1):
        get_score = S[d-1][t-1]
        score += get_score
        contest_last_opened[t-1] = d
        loss_score = 0
        for i in range(26):
            ld = contest_last_opened[i]
            loss_score += C[i]*(d-ld)
        score -= loss_score
    return score


def update_score(D, C, S, T, score, ct, ci):
    """
    ct日目のコンテストをコンテストciに変更する
    スコアを差分更新する

    ct: change t 変更日
    ci: change i 変更コンテスト
    """
    contest_last_opened = [0]*26  # コンテストiを前回開催した日
    for d in range(1, ct):
        contest_last_opened[T[d-1]-1] = d

    prei = T[ct-1]  # 変更前に開催する予定だったコンテストi
    prei_ld = contest_last_opened[prei-1]  # preiが前回開催した日
    preci_ld = contest_last_opened[ci-1]  # ciが前回開催した日
    score -= S[ct-1][prei-1]
    score += S[ct-1][ci-1]

    for d in range(ct, D+1):
        if d != ct and T[d-1] == prei:
            break
        score += C[prei-1]*(d - ct)
        score -= C[prei-1]*(d - prei_ld)

    for d in range(ct, D+1):
        if d != ct and T[d-1] == ci:
            break
        score += C[ci-1]*(d - preci_ld)
        score -= C[ci-1]*(d - ct)
    T[ct-1] = ci
    return score, T


def local_search():
    pass


def main(D, C, S):
    T = []
    for d in range(1, D+1):
        # d日目に一番満足度が高いコンテストを開催する 1-indexed
        # S[d-1]で最大のコンテストiを選ぶ　→ 0点！w
        # d日目にコンテストiを選んだ時に一番スコアが高くなるiを選ぶ
        today_score = calc_score(D, C, S, T + [1])
        today_contest = 1
        for i in range(2, 26 + 1):
            tmp_score = calc_score(D, C, S, T + [i])
            if today_score < tmp_score:
                today_score = tmp_score
                today_contest = i
        T.append(today_contest)
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
