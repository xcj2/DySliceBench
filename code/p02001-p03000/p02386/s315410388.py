import itertools


class Dice():
    def __init__(self, dice_labels):
        self.label = {
            'top': dice_labels[0],
            'south': dice_labels[1],
            'east': dice_labels[2],
            'west': dice_labels[3],
            'north': dice_labels[4],
            'bottom': dice_labels[5]
        }

    def roll(self, str_direction):
        if str_direction == 'E':
            self.__roll_to_east()
        elif str_direction == 'W':
            self.__roll_to_west()
        elif str_direction == 'S':
            self.__roll_to_south()
        elif str_direction == 'N':
            self.__roll_to_north()

    def turn(self, str_direction):
        if str_direction == 'L':
            self.__turn_left()
        elif str_direction == 'R':
            self.__turn_right()

    def __roll_to_east(self):
        self.label['top'], self.label['east'], self.label['west'], self.label['bottom'] = (self.label['west'], self.label['top'], self.label['bottom'], self.label['east'])

    def __roll_to_west(self):
        self.label['top'], self.label['east'], self.label['west'], self.label['bottom'] = (self.label['east'], self.label['bottom'], self.label['top'], self.label['west'])

    def __roll_to_south(self):
        self.label['top'], self.label['south'], self.label['north'], self.label['bottom'] = (self.label['north'], self.label['top'], self.label['bottom'], self.label['south'])

    def __roll_to_north(self):
        self.label['top'], self.label['south'], self.label['north'], self.label['bottom'] = (self.label['south'], self.label['bottom'], self.label['top'], self.label['north'])

    def __turn_right(self):
        self.label['south'], self.label['east'], self.label['west'], self.label['north'] = (self.label['east'], self.label['north'], self.label['south'], self.label['west'])

    def __turn_left(self):
        self.label['south'], self.label['east'], self.label['west'], self.label['north'] = (self.label['west'], self.label['south'], self.label['north'], self.label['east'])


def check_same_surface(dice1, dice2):
    for direction in ['top', 'bottom', 'east', 'west', 'south', 'north']:
        if dice1.label[direction] != dice2.label[direction]:
            return False
    return True


def check_same_dice(dice1, dice2):
    same_pattern_list = []
    for turn_lr in ['R'] * 4:
        for roll_sn in ['N'] * 4:
            for roll_ew in ['E'] * 4:
                dice2.roll(roll_ew)
                same_pattern_list.append(check_same_surface(dice1, dice2))
            dice2.roll(roll_sn)
            same_pattern_list.append(check_same_surface(dice1, dice2))
        dice2.turn(turn_lr)
        same_pattern_list.append(check_same_surface(dice1, dice2))
    return True in same_pattern_list


num_dices = int(input())
dices = []
for dice_number in range(0, num_dices):
    dice_labels = input().split(' ')
    dices.append(Dice(dice_labels))

is_same_dice_result_list = []
for dice1, dice2 in itertools.combinations(dices, 2):
    is_same_dice_result_list.append(check_same_dice(dice1, dice2))

if True in is_same_dice_result_list:
    print('No')
else:
    print('Yes')
