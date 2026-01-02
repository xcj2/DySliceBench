# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_C&lang=jp
sample_input = list(range(3))
sample_input[0] = '''5
H4 C9 S4 D2 C3'''
sample_input[1] = '''2
S1 H1'''
sample_input[2] = '''5
H4 C9 S4 D2 C3'''
give_sample_input = None
if give_sample_input is not None:
    sample_input_list = sample_input[give_sample_input].split('\n')
    def input():
        return sample_input_list.pop(0)
        
# main
import copy

def swap_list_item(lst, i, j):
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp
    
class Card:
    number = None
    mark = None
    def __init__(self, str_card):
        self.number = int(str_card[1])
        self.mark = str_card[0]
        pass
    def __eq__(self, other):
        return self.number == other.number
    def __lt__(self, other):
        return self.number < other.number
    def to_str(self):
        return self.mark + str(self.number)

def selection_sort(list_of_data):
    num_of_data = len(list_of_data)
    for i in range(num_of_data):
        minj = i
        for j in range(i, num_of_data):
            if list_of_data[minj] > list_of_data[j]:
                minj = j
        if not minj == i:
            swap_list_item(list_of_data, i, minj)
            
def bubble_sort(list_of_data):
    flag = True
    while flag:
        flag = False
        n = num_of_data - 1
        while n >= 1:
            if list_of_data[n] < list_of_data[n-1]:
                swap_list_item(list_of_data, n, n-1)
                flag = True
            n -= 1
        
def get_mark_order_info(card_list, number):
    result = ''
    for card in card_list:
        if card.number == number:
            result += card.mark
    return result

def print_card_list(card_list):
    output = ''
    for card in card_list:
        output += card.to_str() + ' '
    output = output.rstrip()
    print(output)

num_of_data = int(input())
data_list_str = input().split()
data_cards = [Card(str) for str in data_list_str]
data_cards_bubble = copy.copy(data_cards)
data_cards_selection = copy.copy(data_cards)

mark_order_info = []
for number in [n+1 for n in range(13)]:
    mark_order_info.append(get_mark_order_info(data_cards, number))
    
bubble_sort(data_cards_bubble)
selection_sort(data_cards_selection)

mark_order_info_bubble = []
for number in [n+1 for n in range(13)]:
    mark_order_info_bubble.append(get_mark_order_info(data_cards_bubble, number))

mark_order_info_selection = []
for number in [n+1 for n in range(13)]:
    mark_order_info_selection.append(get_mark_order_info(data_cards_selection, number))
    
print_card_list(data_cards_bubble)
if (mark_order_info == mark_order_info_bubble):
    print('Stable')
else:
    print('Not stable')
    
print_card_list(data_cards_selection)
if (mark_order_info == mark_order_info_selection):
    print('Stable')
else:
    print('Not stable')