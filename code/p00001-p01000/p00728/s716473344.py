from pprint import pprint as pp
from pprint import pformat as pf
import math

def get_data():
    input_data = int(input())
    return input_data

def make_score_list(referee_num):
    score_list = [None] * referee_num
    for i in range(referee_num):
        score_list[i] = get_data()
    return score_list

def calculate_adjusted_average(score_list, referee_num):
    referee_num -= 2
    adjusted_average = (sum(score_list) - max(score_list) - min(score_list)) / referee_num
    return adjusted_average


if __name__ == "__main__":
    while True:
        referee_num = get_data()
        if referee_num == 0:
            break
        score_list = make_score_list(referee_num)
        adjusted_average = math.floor(calculate_adjusted_average(score_list, referee_num))
        print(adjusted_average)


