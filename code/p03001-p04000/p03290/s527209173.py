from itertools import combinations

def exclude_combi_idx(combis, scores):
    a = [score[1] for score in combis]
    v = []
    for score in scores:
        if score[1] in a:
            continue
        v.append(score)
    return v

def set_all_solve(combi):
    current = 0
    num = 0
    for item in combi:
        num += item[0]
        current += item[2]
    return num, current

def track_residue(num, score, current, target):
    for i in range(num):
        current += score
        if current >= target:
            return i + 1
    return None

def main():
    D, G = [int(c) for c in input().split()]
    items = []
    for idx in range(1, 1+D):
        num, bonasu = [int(c) for c in input().split()]
        items.append((idx * 100, num, bonasu))
    scores = [(num, idx,idx * num + bonasu) for idx, num, bonasu in items]
    max_prob = sum([num for num,_, _ in scores])
    min_prob = max_prob
    for i in range(0, D+1):
        combis = list(combinations(scores, i))
        # print('i = {}, combinations = {}'.format(i, combis))
        for combi in combis:
            s = 0
            prob = 0
            # print('combi = {}'.format(combi))
            tmp, tmp2 = set_all_solve(combi)
            prob += tmp
            s += tmp2
            # print('all solves num = {} score = {}'.format(prob, s))
            if s >= G:
                if prob < min_prob:
                    min_prob = prob
                    continue
            else:
                v = exclude_combi_idx(combi, scores)[-1] # 値が最大のもののみ必要
                res = track_residue(v[0], v[1], s, G)
                if res is None:
                    continue
                if res + prob < min_prob:
                    # print('track solve: num = {}, score = {}'.format(res + prob, s))
                    min_prob = res + prob
    print(min_prob)

if __name__ == '__main__':
    main()