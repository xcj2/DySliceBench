import math
TICKET_PRICE = 100


def get_data_list():
    data_list = input().split()
    for i in range(len(data_list)):
        data_list[i] = int(data_list[i])
    return data_list

def get_input():
    input_data = int(input())
    return input_data

def make_ticket_dict(player):
    ticket_sum = 0
    ticket_list = dict()
    order = 1
    for i in range(player):
        input_data = get_input()
        ticket_list[order] = input_data
        order += 1
    return ticket_list

def calculate_distribution_money(ticket_list, deduction_rate):
    ticket_sum = 0
    for ticket_num in ticket_list.values():
        ticket_sum += ticket_num
    sum_money = ticket_sum * TICKET_PRICE
    distribution_money = sum_money * (100 - deduction_rate) / 100
    return distribution_money


if __name__ == "__main__":
    while True:
        data_list = get_data_list()
        if data_list[0] == 0:
            break
        player = data_list[0]
        winner = data_list[1]
        deduction_rate = data_list[2]
        ticket_list = make_ticket_dict(player)
        if ticket_list[winner] == 0:
            print(0)
            continue
        distribution_money = calculate_distribution_money(ticket_list, deduction_rate)
        each_distribution_money = math.floor(distribution_money / ticket_list[winner])
        print(each_distribution_money)

