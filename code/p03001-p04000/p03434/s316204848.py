# coding: utf-8
"""this is python work script"""

def find_score(N, card_list):
    """return score list about a and b"""
    sum_a, sum_b = 0, 0
    card_list.sort()
    for i in range(N):
        if i % 2 == 0:
            sum_a += card_list.pop()
        else:
            sum_b += card_list.pop()
    return sum_a, sum_b

def solve(num, card_list):
    """solve problem"""
    a_score, b_score = find_score(num, card_list)
    diff_score = a_score - b_score
    return diff_score

def main():
    """main method"""
    num_cards = int(input())
    list_cards = list(map(int, input().split(' ')))
    answer = solve(num_cards, list_cards)
    print(answer)

if __name__ == '__main__':
    main()
