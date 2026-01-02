class Dice:
    __slots__ = ['n_list', 'pair_list']

    def __init__(self, n_tup):
        self.n_list = list(n_tup)
        self.pair_list = [self.return_dice_round_pair(self.n_list, 2, 3, 5, 4),
                          self.return_dice_round_pair(self.n_list, 1, 4, 6, 3),
                          self.return_dice_round_pair(self.n_list, 1, 2, 6, 5),
                          self.return_dice_round_pair(self.n_list, 1, 5, 6, 2),
                          self.return_dice_round_pair(self.n_list, 1, 3, 6, 4),
                          self.return_dice_round_pair(self.n_list, 2, 4, 5, 3)
                          ]

    @staticmethod
    def roll_switch(n_list, from_idx_list, to_idx_list):
        n_list[from_idx_list[0] - 1], \
        n_list[from_idx_list[1] - 1], \
        n_list[from_idx_list[2] - 1], \
        n_list[from_idx_list[3] - 1] \
            = n_list[to_idx_list[0] - 1], \
              n_list[to_idx_list[1] - 1], \
              n_list[to_idx_list[2] - 1], \
              n_list[to_idx_list[3] - 1]
        return n_list

    def roll(self, direction):
        if direction == "N":
            self.n_list = self.roll_switch(self.n_list, [1, 2, 6, 5], [2, 6, 5, 1])

        elif direction == "E":
            self.n_list = self.roll_switch(self.n_list, [1, 3, 6, 4], [4, 1, 3, 6])

        if direction == "S":
            self.n_list = self.roll_switch(self.n_list, [1, 2, 6, 5], [5, 1, 2, 6])

        if direction == "W":
            self.n_list = self.roll_switch(self.n_list, [1, 3, 6, 4], [3, 6, 4, 1])

    def spin(self):
        self.n_list = self.roll_switch(self.n_list, [2, 3, 5, 4], [3, 5, 4, 2])

    @staticmethod
    def return_dice_round_pair(n_list, a, b, c, d):
        return [(n_list[a - 1], n_list[b - 1]),
                (n_list[b - 1], n_list[c - 1]),
                (n_list[c - 1], n_list[d - 1]),
                (n_list[d - 1], n_list[a - 1])]

    def return_right_num(self, top, forward):
        for i in range(6):
            if (top, forward) in self.pair_list[i]:
                return self.n_list[i]


def comparison_dice(dice_src, dice_tmp):
    # ?????¢????????????
    def compare_back(dice_tmp, dice_src):
        if dice_tmp.n_list[5] != dice_src.n_list[5]:
            return False
        else:
            if compare_with_spin(dice_tmp, dice_src):
                return True
            else:
                return False

    def compare_with_spin(dice_tmp, dice_src):
        # ??????4??¢???????????????????????§spin?????????
        for k in range(4):
            dice_tmp.spin()
            if dice_tmp.n_list == dice_src.n_list:
                print("Yes")
                return True
        else:
            return False

    # ?????¢???????????????
    for i in range(4):
        dice_tmp.roll("W")
        if dice_tmp.n_list[0] == dice_src.n_list[0]:
            if compare_back(dice_tmp, dice_src):
                break
    else:
        for j in range(4):
            dice_tmp.roll("N")
            if dice_tmp.n_list[0] == dice_src.n_list[0]:
                if compare_back(dice_tmp, dice_src):
                    break
        else:
            print("No")

dice_src = Dice([int(x) for x in input().split()])
dice_tmp = Dice([int(x) for x in input().split()])
comparison_dice(dice_src, dice_tmp)