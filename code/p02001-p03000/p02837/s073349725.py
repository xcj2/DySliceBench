from collections import defaultdict


def is_testimony_correct(hypothesis, testimony):
    # 証言の対象者が仮説上、正直者となっているかを検証。
    for target, is_honest in testimony.items():
        if int(hypothesis[target]) == is_honest:
            continue
        return False
    return True


def is_hypothesis_correct(hypothesis, testimony_dict):
    for witness_num, testimony in testimony_dict.items():
        # 仮説上の正直者の証言だけ検証する
        if hypothesis[witness_num] == "1":
            # 証言を検証
            if is_testimony_correct(hypothesis, testimony):
                continue
            else:
                # 証言に誤りがある場合、Falseで抜ける
                return False
    return True


def main():
    N = int(input())
    testimony_dict = defaultdict(dict)

    # 証人ごとに証言をdictで保存
    for witness_num in range(N):
        for _ in range(int(input())):
            target, is_honest = list(map(int, input().split()))
            testimony_dict[witness_num][target - 1] = is_honest

    # 仮説を検証  e.g.'010010' 正直者が2人 (witness_num =1, 4)
    max_count = 0
    for i in range(1, 2**N):
        # 仮説を01で表現
        hypothesis = format(i, 'b').zfill(N)
        # 仮説が正しい場合のみ、正直者の数でmax_countを更新
        if is_hypothesis_correct(hypothesis, testimony_dict):
            max_count = max(max_count, hypothesis.count(str("1")))
    print(max_count)


if __name__ == '__main__':
    main()