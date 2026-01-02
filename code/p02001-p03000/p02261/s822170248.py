class Card():

    def __init__(self):
        self.suit = 0
        self.value = 0


def bubble_sort(c, n):
    for i in range(n):
        for j in range(n - 1, i, -1):
            if c[j].value < c[j - 1].value:
                c[j], c[j - 1] = c[j - 1], c[j]


def selection_sort(c, n):
    for i in range(n):
        minj = i
        for j in range(i, n):
            if c[j].value < c[minj].value:
                minj = j
        c[i], c[minj] = c[minj], c[i]


def is_stable(c1, c2, n):
    for i in range(n):
        if c1[i].suit != c2[i].suit:
            return False
    return True


def print_result(c, n):
    r = []
    for i in range(n):
        r.append(c[i].suit + str(c[i].value))
    print(' '.join(r))


def main():
    n = int(input())
    c1 = [Card() for x in range(n)]
    c2 = [Card() for x in range(n)]
    ary = [x for x in input().split(' ')]

    for i in range(n):
        s, v = list(ary[i])
        c1[i].suit, c1[i].value = s, int(v)
        c2[i].suit, c2[i].value = s, int(v)

    bubble_sort(c1, n)
    selection_sort(c2, n)

    print_result(c1, n)
    print('Stable')
    print_result(c2, n)
    if is_stable(c1, c2, n):
        print('Stable')
    else:
        print('Not stable')


if __name__ == '__main__':
    main()