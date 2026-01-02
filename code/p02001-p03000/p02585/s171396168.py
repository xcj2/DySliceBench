def li():
    return [int(x) for x in input().split()]

N, K = li()
P = [0] + li()
C = [0] + li()

def get_cycle(start_i):
    cycle = []
    i = start_i
    while True:
        i = P[i]
        if i == start_i:
            break
        cycle.append(i)
    cycle.append(start_i)
    return cycle

def get_cycle_scores(cycle):
    score = 0
    scores = [score]
    for i in cycle:
        score += C[i]
        scores.append(score)
    return scores

max_scores = []
for start_i in range(1,N+1):
    cycle = get_cycle(start_i)
    scores = get_cycle_scores(cycle)
    cycle_len = len(cycle)
    score_per_cycle = scores[cycle_len]
    # 1cycle以下の場合は全て調べればよし
    if K <= len(cycle):
        max_score = max(scores[move] for move in range(1, K+1))
        max_scores.append(max_score)
        continue
    # 1サイクルごとのスコアがマイナスならサイクルを回らないのがハイスコア
    if score_per_cycle <= 0:
        max_score = max(scores[move] for move in range(1, cycle_len+1))
        max_scores.append(max_score)
        continue
    # 1サイクルごとのスコアがプラスなら限界までサイクルを回るのがハイスコア
    # ラスト1cycleのスコアを調べる
    scores_last_cycle = []
    for move in range(K-cycle_len+1, K+1):
        # 何周したか
        loop_cnt = move // cycle_len
        # あまり
        rest_move = move % cycle_len
        # スコア = 1周ごとのスコア * 何周したか + あまり
        score = loop_cnt * score_per_cycle + scores[rest_move]
        scores_last_cycle.append(score)

    max_scores.append(max(scores_last_cycle))

print(max(max_scores))

