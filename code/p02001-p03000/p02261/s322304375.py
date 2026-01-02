N = int(input())
C1 = list(input().split()) 
C2 = C1[:]

def get_card_suit(card):
    return card[:1]

def get_card_value(card):
    return card[1:]

def bubble_sort(card):
    r_exists = True

    while r_exists == True:

        r_exists = False

        i = N - 1

        while i >= 1:

            if get_card_value(card[i]) < get_card_value(card[i - 1]):
                
                card[i], card[i - 1] = card[i - 1], card[i]

                r_exists = True
            
            i -= 1

def select_sort(card):
    i = 0

    while i < N:

        min_j = i
        j = i

        while j < N:

            if get_card_value(card[j]) < get_card_value(card[min_j]):

                min_j = j

            j += 1

        card[i], card[min_j] = card[min_j], card[i]

        i += 1

def output(card):
    s = ''

    for x in card:

        s = s + str(x) + ' '

    print(s.rstrip())

def is_stable():
    i = 0

    while i < N:
        if get_card_suit(C1[i]) != get_card_suit(C2[i]):
            return False
        i += 1
    
    return True

bubble_sort(C1)
select_sort(C2)

output(C1)
print('Stable')

output(C2)
if is_stable() == True:
    print('Stable')
else:
    print('Not stable')

