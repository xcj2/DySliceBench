import collections

def solution1(kard):
    #強いものから順に探していく
    if fourcard(kard):
        print("four card")
    elif fullhouse(kard):
        print("full house")
    elif straight(kard):
        print("straight")
    elif threecard(kard):
        print("three card")
    elif twopair(kard):
        print("two pair")
    elif onepair(kard):
        print("one pair")
    else:
        print("null")

def fourcard(kard):
    if kard.count(kard[0])==4 or kard.count(kard[1])==4:
        return True
    else:
        return False

def fullhouse(kard):
    list=collections.Counter(kard)
    if len(list)==2:
        return True
    else:
        return False

def straight(kard):
    c=sorted(kard,reverse=True)
    if c[0]==(c[1]+1)==(c[2]+2)==(c[3]+3)==(c[4]+4) or (c[0]==(c[1]+1)==(c[2]+2)==(c[3]+3) and c[4]==1 and c[0]==13):
        return True
    else:
        return False
    

def threecard(kard):
    if kard.count(kard[0])==3 or kard.count(kard[1])==3 or kard.count(kard[2])==3:
        return True
    else:
        return False
    
def twopair(kard):
    list=collections.Counter(kard)
    if len(list)==3:
        return True
    else:
        return False

def onepair(kard):
    list=collections.Counter(kard)
    if len(list)==4:
        return True
    else:
        return False


while True:
    try:
        kard=list(map(int,input().split(",")))
    except:
        break
    solution1(kard)

