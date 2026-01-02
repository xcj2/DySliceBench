def sgn(a, b):
    return int(a*b/abs(a*b))

class Dice:
    def __init__(self, numbers):
        self.numbers_dict = {1:numbers[0], 2:numbers[1], 3:numbers[2], -3:numbers[3], -2:numbers[4], -1:numbers[5]}
        self.numbers_ver_dict = {numbers[0]:1, numbers[1]:2,numbers[2]:3,numbers[3]:-3, numbers[4]:-2,numbers[5]:-1}

    # a:top, b:front
    def show_right(self, a, b):
        var_a = self.numbers_ver_dict[a]
        var_b = self.numbers_ver_dict[b]
        if abs(var_a) == 1:
            if abs(var_b) == 2:
                return self.numbers_dict[sgn(var_a,var_b)*3]
            else:
                return self.numbers_dict[-sgn(var_a,var_b)*2]
        elif abs(var_a) == 2:
            if abs(var_b) == 1:
                return self.numbers_dict[-sgn(var_a, var_b)*3]
            else:
                return self.numbers_dict[sgn(var_a,var_b)]
        else:
            if abs(var_b) == 1:
                return self.numbers_dict[sgn(var_a, var_b)*2]
            else:
                return self.numbers_dict[-sgn(var_a,var_b)]

if __name__ == '__main__':
    examin_list = list(map(int, input().split()))
    dice1 = Dice(examin_list)
    dice2 = Dice(list(map(int, input().split())))
    yes_flag = True
    exam_tuple = ((examin_list[0], examin_list[1]), (examin_list[0], examin_list[2]), (examin_list[0], examin_list[4]),
                  (examin_list[0], examin_list[3]), (examin_list[1], examin_list[5]))
    for num in exam_tuple:
        if dice1.show_right(num[0], num[1]) != dice2.show_right(num[0], num[1]):
            print('No')
            yes_flag = False
            break
    if yes_flag:
        print('Yes')

