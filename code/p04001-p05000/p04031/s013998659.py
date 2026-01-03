
import math

def read_input():
    n = int(input())
    alist = list(map(int, input().split()))
    return n, alist


def calc_se(t, alist):
    return sum([(t - a) ** 2 for a in alist])


def submit():
    n, alist = read_input()
    avg_alist = sum(alist)/n

    cand1 = math.floor(avg_alist)
    cand2 = math.ceil(avg_alist)

    if cand1 == cand2:
        se = calc_se(cand1, alist)
    else:
        se1 = calc_se(cand1, alist)
        se2 = calc_se(cand2, alist)
        se = min(se1, se2)

    print(se)

if __name__ == '__main__':
    submit()
