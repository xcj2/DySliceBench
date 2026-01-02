input_data = input().split(" ")
items = [int(cont) for cont in input_data]
keys = ['T', 'S', 'E', 'W', 'N', 'B']
dice = dict(zip(keys, items))

def q1():
    def rot_func_list(rot, dice):
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

    controls = list(input())
    for i in controls:
        rot_func_list(i, dice)
    print(dice["T"])

def q2():

    def search_surf(conds, dice):
        a,b=conds
        a_key = [k for k, v in dice.items() if v == a ]
        b_key = [k for k, v in dice.items() if v == b ]
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

    a = input()
    repeater = int(a)

    for neee in range(repeater):
        control_input = input().split(" ")
        conds = [int(i) for i in control_input]
        search_surf(conds, dice)

q2()

