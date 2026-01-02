import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    n = input_int()
    testimonies = []
    for _ in range(n):
        a = input_int()
        testimony = []
        for _ in range(a):
            x, y = input_int_list()
            testimony.append([x, y])
        testimonies.append(testimony)
    # すべてのパターンを試すO(2**n)
    ans = 0
    for i in range(2**n):
        sample = [None] * n
        for j in range(n):
            if i >> j & 1:
                sample[j] = 1
            else:
                sample[j] = 0
        sample = [None] + sample  # 1-indexed
        # sampleが成立するか確認する
        is_possible = True
        for idx, testimony in enumerate(testimonies):
            if sample[idx + 1] == 1:
                for x, y in testimony:
                    if sample[x] == y:
                        continue
                    else:
                        is_possible = False
        # すべての証言が正しければ、正直者の数を答えにする
        if is_possible:
            ans = max(ans, sum(sample[1:]))
    print(ans)

    return


if __name__ == "__main__":
    main()
