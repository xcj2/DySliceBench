card = []
for _ in range(3):
    line = list(map(int, input().split()))
    card.append(line)

check_card = [[False, False, False] for i in range(3)]


def check(num):
    for y in range(3):
        for x in range(3):
            if card[y][x] == num:
                check_card[y][x] = True


n = int(input())
for _ in range(n):
    num = int(input())
    check(num)


def ver(check_card):
    for x in range(3):
        res = [check_card[0][x], check_card[1][x], check_card[2][x]]
        if sum(res) == 3:
            return True
    return False


def hor(check_card):
    for y in range(3):
        res = check_card[y]
        if sum(res) == 3:
            return True
    return False


def naname(check_card):
    pat1 = check_card[0][0] + check_card[1][1] + check_card[2][2]
    pat2 = check_card[0][2] + check_card[1][1] + check_card[2][0]
    if pat1 == 3 or pat2 == 3:
        return True
    else:
        return False


if ver(check_card) or hor(check_card) or naname(check_card):
    print('Yes')
else:
    print('No')