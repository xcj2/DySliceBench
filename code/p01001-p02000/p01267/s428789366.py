class SlotMachine:
    def __init__(self, reel_num, A, B, C):
        self.reel_num = reel_num
        self.A = A
        self.B = B
        self.C = C
    def calculate_random_num(self, random_num):
        random_num = (self.A * random_num + self.B) % self.C
        # print("random_num", random_num) # debug
        return random_num

    def count_flame(self, condition_list, random_num) :
        flame_num = 0
        order = 0
        while order < len(condition_list):
            order, flame_num, random_num = self.check_condition(condition_list, random_num, order, flame_num)
            if flame_num > 10001:
                flame_num = -1
                return flame_num
        return flame_num - 1

    def check_condition(self, condition_list, random_num, order, flame_num):
        if random_num == condition_list[order]:
            order += 1
        random_num = self.calculate_random_num(random_num)
        flame_num += 1
        # print("flame_num", flame_num) # debug
        return order, flame_num, random_num




def get_data_list():
    data_list = input().split()
    for i in range(len(data_list)):
        data_list[i] = int(data_list[i])
    return data_list


if __name__ == "__main__":
    while True:
        data_list = get_data_list()
        # print("data_list", data_list) # debug
        reel_num = data_list[0]
        A = data_list[1]
        B = data_list[2]
        C = data_list[3]
        first_num = data_list[4]
        if reel_num == 0:
            break
        condition_list = get_data_list()
        slot_machine = SlotMachine(reel_num, A, B, C)
        flame_num = slot_machine.count_flame(condition_list, first_num)
        # print("ans", flame_num) # debug
        print(flame_num)


