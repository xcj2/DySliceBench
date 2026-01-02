import sys

def is_onepair(x):
    for i in range(4):
        if x.count(x[i]) == 2:
            return True

    return False

def is_twopair(x):
    count = 0
    i = 0
    x.sort()
    while i < 5:
        if x.count(x[i]) == 2:
            i += 2
            count += 1
        else:
            i += 1
        if count == 2:
            return True

    return False

def is_threecard(x):
    for i in range(3):
        if x.count(x[i]) == 3:
            return True

    return False

def is_straight(x):
    x.sort()
    if x[0] == 1 and x[1:] == [10, 11, 12, 13]:
        return True
    for i in range(4):
        if x[i]+1 != x[i+1]:
            return False
    
    return True

def is_fullhouse(x):
    if is_threecard(x) and is_onepair(x):
        return True

    return False
    
def is_fourcard(x):
    for i in range(2):
        if x.count(x[i]) == 4:
            return True

    return False

for line in sys.stdin.readlines():
    hand = list(map(int, line.split(',')))
    if is_fourcard(hand):
        print("four card")
    elif is_fullhouse(hand):
        print("full house")
    elif is_straight(hand):
        print("straight")
    elif is_threecard(hand):
        print("three card")
    elif is_twopair(hand):
        print("two pair")
    elif is_onepair(hand):
        print("one pair")
    else:
        print("null")