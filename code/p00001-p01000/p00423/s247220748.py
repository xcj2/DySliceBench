def judge_game_set(game_num):
    a_point, b_point = 0, 0
    for _ in range(game_num):
        a_point, b_point = judge_game(a_point, b_point)
    print(a_point, b_point, sep=' ')

def judge_game(a_point, b_point):
    a_card, b_card = map(int, input().split(' '))

    if a_card > b_card:
        a_point += (a_card + b_card)
    elif a_card < b_card:
        b_point += (a_card + b_card)
    else:
        a_point += a_card
        b_point += b_card

    return a_point, b_point

def judge_game_sets():
    game_num = int(input())
    while game_num != 0:
        judge_game_set(game_num)
        game_num = int(input())

if __name__ == '__main__':
    judge_game_sets()

