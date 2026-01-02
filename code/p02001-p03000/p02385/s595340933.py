import itertools
def get_dice():
    input_data = input().split(" ")
    items = [int(cont) for cont in input_data]
    keys = ['T', 'S', 'E', 'W', 'N', 'B']
    return dict(zip(keys, items))

def rot_dice(rot, dice):
    if rot == "N":
        keys = ['T', 'S', 'B', 'N']
        items = dice['S'], dice['B'], dice['N'], dice['T']
        new_dice = dict(zip(keys, items))
        dice.update(new_dice)

    if rot == "S":
        keys = ['T', 'S', 'B', 'N']
        items = dice['N'], dice['T'], dice['S'], dice['B']
        new_dice = dict(zip(keys, items))
        dice.update(new_dice)

    if rot == "E":
        keys = ['T', 'E', 'B', 'W']
        items = dice['W'], dice['T'], dice['E'], dice['B']
        new_dice = dict(zip(keys, items))
        dice.update(new_dice)

    if rot == "W":
        keys = ['T', 'E', 'B', 'W']
        items = dice['E'], dice['B'], dice['W'], dice['T']
        new_dice = dict(zip(keys, items))
        dice.update(new_dice)

    if rot == "R":
        keys = ['N', 'W', 'S', 'E']
        items = dice['E'], dice['N'], dice['W'], dice['S']
        new_dice = dict(zip(keys, items))
        dice.update(new_dice)

def search_right_surf(conds, dice):
    a, b = conds
    a_key = [k for k, v in dice.items() if v == a]
    b_key = [k for k, v in dice.items() if v == b]
    key_list = a_key + b_key

    part_st = ''.join(key_list)

    def search(part_st):
        if part_st in "TNBST":
            return "W"

        if part_st in "TSBNT":
            return "E"

        if part_st in "TEBWT":
            return "N"

        if part_st in "TWBET":
            return "S"

        if part_st in "NESWN":
            return "B"

        if part_st in "NWSEN":
            return "T"

    target_key = search(part_st)
    print(dice[target_key])

def search_top_surf(top_surf, dice):

    dice2_surf, *_ = [k for k, v in dice.items() if v == top_surf]

    if dice2_surf == 'N':
        rot_dice("S", dice)

    if dice2_surf == 'B':
        controls = list("SS")
        for i in controls:
            rot_dice(i, dice)
    if dice2_surf == 'S':
        controls = list("N")
        for i in controls:
            rot_dice(i, dice)
    if dice2_surf == 'W':
        controls = list("E")
        for i in controls:
            rot_dice(i, dice)
    if dice2_surf == 'E':
        controls = list("W")
        for i in controls:
            rot_dice(i, dice)

def search_flont_surf(flont_surf, dice):

    dice2_surf, *_ = [k for k, v in dice.items() if v == flont_surf]

    if dice2_surf == 'E':
        controls = list("R")
        for i in controls:
            rot_dice(i, dice)

    if dice2_surf == 'S':
        controls = list("RR")
        for i in controls:
            rot_dice(i, dice)

    if dice2_surf == 'W':
        controls = list("RRR")
        for i in controls:
            rot_dice(i, dice)

def perfect_rot_compare(dice1, dice2):

        def compare_dice():
            if dice1 == dice2:
                return True
        if compare_dice():
            return True
        Rs = ["", "R", "RR", "RRR", "RRRR"]
        Ns = ["", "N", "NN", "NNN", "NNNN"]
        Es = ["", "E", "EE", "EEE", "EEEE"]
        for i, j, k in itertools.product(Rs, Ns, Es):
            controls = list(i+j+k)
            for t in controls:
                rot_dice(t, dice2)
            if compare_dice():
                return True
        return False


def q1():

    dice=get_dice()
    controls = list(input())
    for i in controls:
        rot_dice(i, dice)
    print(dice["T"])

def q2():

    dice=get_dice()
    a = input()
    repeater = int(a)

    for neee in range(repeater):
        control_input = input().split(" ")
        conds = [int(i) for i in control_input]
        search_right_surf(conds, dice)

def q3():
    dice1 = get_dice()
    dice2 = get_dice()

    if perfect_rot_compare(dice1, dice2):
        print("Yes")
    else:
        print("No")

def q4():
    inp = input()
    dice_num = int(inp)
    dice_list = list()
    for i in range(dice_num):
        dice_list.append(get_dice())

    def compare_many_dices():
        dice1 = dice_list[0]
        for dice in dice_list:
            if not perfect_rot_compare(dice1, dice):
                return False
        return True

    if compare_many_dices():
        print("Yes")
    else:
        print("No")

q3()
