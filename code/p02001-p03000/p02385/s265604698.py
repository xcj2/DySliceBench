mask = [[i for i in range(6)], (1, 5, 2, 3, 0, 4), (2, 1, 5, 0, 4,3),(3, 1, 0, 5, 4, 2), (4, 0, 2, 3, 5, 1)]
mask += [[mask[1][i] for i in mask[1]]]
 
def set_top(dice, top):
    return [dice[i] for i in mask[top]]
 
def twist(dice):
    return [dice[i] for i in (0, 3, 1, 4, 2, 5)]
 
def equal(dice1, dice2):
    for i in range(6):
        tmp_dice = set_top(dice2, i)
        for _ in range(4):
            if dice1 == tmp_dice:
                return True
            tmp_dice = twist(tmp_dice)
    return False
         
dice1 = input().split()
dice2 = input().split()
 
print('Yes' if equal(dice1, dice2) else 'No')
