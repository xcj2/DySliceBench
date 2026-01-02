
trump_card = [[0 for i in range(13)] for j in range(4)]

def get_type_index(type_str):
    if type_str == 'S':
        return 0
    elif type_str == 'H':
        return 1
    elif type_str == 'C':
        return 2
    else:
        return 3

def get_type_str(type_index):
    if type_index == 0:
        return 'S'
    elif type_index == 1:
        return 'H'
    elif type_index == 2:
        return 'C'
    else:
        return 'D'

def is_exist_card(type_index, num):
    return trump_card[type_index][num - 1] == 1

def set_card(type_str, num):
    type_index = get_type_index(type_str)
    trump_card[type_index][num - 1] = 1

N = int(input())
for i in range(N):
    type_str, card_num_str = input().split()
    set_card(type_str, int(card_num_str))

for type_index in range(len(trump_card)):
    for num in range(1, len(trump_card[type_index]) + 1):
        if not is_exist_card(type_index, num):
            print(get_type_str(type_index), num)

