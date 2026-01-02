def get_input():
    input_data = int(input())
    return input_data

def get_data_list():
    data_list = input().split()
    for i in range(len(data_list)):
        data_list[i] = int(data_list[i])
    return data_list

class Checker:
    def __init__(self, sorted_list):
        self.sorted_list = sorted_list
        self.a = 0
        self.b = 1
        self.min_num = float("inf")
        self.try_num = len(self.sorted_list) - 1 # for not subtract last + 1 from last

    def detect_min_num(self):
        for i in range(self.try_num):
            tmp_num = self.sorted_list[self.b] - self.sorted_list[self.a]
            if tmp_num <= self.min_num:
                self.min_num = tmp_num
            self.a, self.b = self.b, self.b + 1


if __name__ == "__main__":
    while True:
        student_num = get_input()
        if student_num == 0:
            break
        data_list = get_data_list()
        sorted_list = sorted(data_list)
        # print("data_list", data_list) # debug
        # print("sorted_list", sorted_list) # debug
        checker = Checker(sorted_list)
        checker.detect_min_num()
        min_num = checker.min_num
        # print("min_num", min_num) # debug
        print(min_num)


