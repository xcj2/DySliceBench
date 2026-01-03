import math


def read_input():
    n = int(input())

    ratios = []
    for i in range(n):
        t, a = map(int, input().split())
        ratios.append((t, a))

    return n, ratios


def get_votes(ex_votes, ratio):
    def check_votes(a, b):
        return a[0] <= b[0] and a[1] <= b[1]

    def div_ceil(a, b):
        if a % b == 0:
            return a //b
        else:
            return a // b + 1

    base = div_ceil(sum(ex_votes), (ratio[0] + ratio[1]))
    base = int(base)
    while True:
        test_votes = (ratio[0] * base, ratio[1] * base)
        if check_votes(ex_votes, test_votes):
            return test_votes
        else:
            diff_votes = (test_votes[0] - ex_votes[0], test_votes[1] - ex_votes[1])
            if diff_votes[0]/ratio[0] < diff_votes[1]/ratio[1]:
                base += div_ceil(-diff_votes[0], ratio[0])
            else:
                base += div_ceil(-diff_votes[1], ratio[1])
            base = int(base)


def submit():
    n, ratios = read_input()

    votes = ratios[0]
    for ratio in ratios[1:]:
        votes = get_votes(votes, ratio)

    print(sum(votes))


if __name__ == '__main__':
    submit()
