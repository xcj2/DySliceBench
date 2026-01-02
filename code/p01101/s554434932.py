from copy import copy

def get_input():
    data_list = input().split()
    for i, v in enumerate(data_list):
        data_list[i] = int(v)
    return data_list


def remove_over_budeget(value_list, budget):
    tmp_list = copy(value_list)
    for i, v in enumerate(tmp_list):
        if v >= budget:
            del value_list[i:]
            return value_list
    return value_list

def get_max_value_list(value_list,budget):
    if value_list == []: # in preperation for all value is over budget
        return "NONE"
    max_value = 0
    for i in range(0, len(value_list)-1):
        for j in range(i+1,len(value_list)):
            # print("j", j) # debug
            # print("i", i) # debug
            combination_plan = value_list[i] + value_list[j]
            if combination_plan <= budget and combination_plan > max_value:
                max_value = combination_plan
    if max_value == 0:
        return "NONE"
    return max_value





if __name__ == "__main__":
    while True:
        item_num, budget = get_input()
        if item_num == 0:
            break
        value_list = get_input()
        value_list.sort()
        value_list = remove_over_budeget(value_list, budget)
        max_value = get_max_value_list(value_list,budget)
        # print("max_value", max_value) # debug
        print(max_value)

