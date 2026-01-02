
def read_input():
    s = list(map(int, list(str(input()))))
    n = len(s)

    return n, s


# 桁数nでtスタートの数列を作成する
def make_answers(n, t):
    curr  = t

    result = []
    for i in range(n):
        result.append(curr)

        if curr == 1:
            curr = 0
        else:
            curr = 1

    return result


# aとbを要素比較して異なる部分を数える
def diff_num_seq(a, b):
    return sum([1 for ae, be in zip(a, b) if ae != be])


if __name__ == '__main__':
    n, s = read_input()

    answer0 = make_answers(n, 0)
    answer1 = make_answers(n, 1)

    diff0 = diff_num_seq(s, answer0)
    diff1 = diff_num_seq(s, answer1)

    answer = min(diff0, diff1)

    print(answer)