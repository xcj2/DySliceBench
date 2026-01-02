
def read_input():
    cards = []
    for i in range(3):
        r = list(map(int, input().split()))
        cards.append(r)

    n = int(input())
    
    blist = []
    for _ in range(n):
        blist.append(int(input()))

    return cards, blist


def get_row(cards, i):
    return cards[i]


def get_col(cards, i):
    col = [cards[j][i] for j in range(3)]
    return col


def get_diag(cards):
    diag = [cards[i][i] for i in range(3)]
    return diag


def get_re_diag(cards):
    diag = [cards[i][2 - i] for i in range(3)]
    return diag


def submit():
    cards, blist = read_input()

    numbers = set(blist)
    bingo = False
    for i in range(3):
        r = get_row(cards, i)
        if set(r) <= numbers:
            print("Yes")
            return

        c = get_col(cards, i)
        if set(c) <= numbers:
            print("Yes")
            return

    if set(get_diag(cards)) <= numbers:
        print("Yes")
        return

    if set(get_re_diag(cards)) <= numbers:
        print("Yes")
        return

    print("No")


if __name__ == "__main__":
    submit()