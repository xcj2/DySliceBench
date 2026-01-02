# coding: utf-8
"""this is python work script"""

def find_score(card_list):
    """return score list about a and b"""
    sum_a, sum_b = 0, 0
    card_list.sort()
    
    for i in range(len(card_list)):
        if i % 2 == 0:
            sum_a += card_list.pop()
        else:
            sum_b += card_list.pop()
            
    return sum_a, sum_b

def solve(card_list):
    """solve problem"""
    a_score, b_score = find_score(card_list)
    diff_score = a_score - b_score
    
    return diff_score

def main():
    """main method"""
    _ = input()
    list_cards = list(map(int, input().split(' ')))
    answer = solve(list_cards)
    print(answer)

if __name__ == '__main__':
    main()
