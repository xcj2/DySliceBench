def fourcard(card) :
    if card.count(card[0]) == 4 or card.count(card[1]) == 4 :
        return True
    else :
        return False

def fullhouse(card) :
    card.sort()
    if (card[0] ==  card[1] == card[2] and card[3] == card[4]) or (card[0] == card[1] and card[2] == card[3] == card[4]) :
        return True
    else :
        return False
        
def straight(card) :
    card.sort()
    if card[0] == 1 and card[1] == 10 and card[2] == 11 and  card[3] == 12 and card[4] == 13 :
        return True
    else :
        ans = 'True'
        for i in range(4) :
            if card[i] + 1 != card[i + 1] :
                ans = False
        if ans == 'True' :
            return True
        else :
            return False

def threecard(card) :
    if card.count(card[0]) == 3 or card.count(card[1]) == 3 or card.count(card[2]) == 3 :
        return True
    else :
        return False
def twopair(card) :
    card.sort()
    if card[0] == card[1] :
        if card[2] == card[3] or card[3] == card[4]:
            return True
    elif card[1] == card[2] :
        if card[3] == card[4] :
            return True
    else :
        return False
def onepair(card) :
    card.sort()
    if card[0] == card[1] or card[1] == card[2] or card[2] == card[3] or card[3] == card[4] :
        return True
    else :
        return False


while True :
    try :
        card = list(map(int, input().split(',')))
    except EOFError :
        break
    
    if fourcard(card) :
        print('four card')
    elif fullhouse(card) :
        print('full house')
    elif straight(card) :
        print('straight')
    elif threecard(card) :
        print('three card')
    elif twopair(card) :
        print('two pair')
    elif onepair(card) :
        print('one pair')
    else :
        print('null')
