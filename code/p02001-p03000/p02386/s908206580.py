mask = [[i for i in range(6)], (1, 5, 2, 3, 0, 4), (2, 1, 5, 0, 4,3),(3, 1, 0, 5, 4, 2), (4, 0, 2, 3, 5, 1)]
mask += [[mask[1][i] for i in mask[1]]]

def set_top(dice, top):
    return [dice[i] for i in mask[top]]

def twist(dice):
    return [dice[i] for i in (0, 3, 1, 4, 2, 5)]

def equal(dice1, dice2):
    if sorted(dice1) != sorted(dice2):
        return False
    
    for i in range(6):
        tmp_dice = set_top(dice2, i)
        for _ in range(4):
            if dice1 == tmp_dice:
                return True
            tmp_dice = twist(tmp_dice)
    return False

def diff_check_all(dices, n):
    for i in range(n -1):
        for j in range(i + 1, n):
            if equal(dices[i], dices[j]):
                return False
    return True
            

n = int(input())
dices = [input().split() for _ in range(n)]

print('Yes' if diff_check_all(dices, n) else 'No')