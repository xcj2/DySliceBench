def create_card_set():
    card_types=["S","H","C","D"]
    cart_nums=[i+1 for i in range(13)]
    
    card_set=set()
    
    for ct in card_types:
        for cn in cart_nums:
            card_set = card_set | {(ct,cn)}
    
    return card_set
    
def read_card():
    n=int(input())
    init_card_set=set()
    
    for i in range(n):
        ct,cn_s=tuple(input().split())
        cn = int(cn_s)
        init_card_set = init_card_set | {(ct,cn)}
        
    return init_card_set
    

def sort_card(left_card):
    #card typeをバケットソート
    spade_ls=[]
    heart_ls=[]
    club_ls=[]
    diamond_ls=[]
    
    for card in left_card:
        ct=card[0]
        if ct=="S":
            spade_ls.append(card)
        elif ct == "H":
            heart_ls.append(card)
        elif ct=="C":
            club_ls.append(card)
        elif ct=="D":
            diamond_ls.append(card)
            
    #カード毎の数字を昇順ソート
    spade_ls=sorted(spade_ls,key=lambda x:x[1])
    heart_ls=sorted(heart_ls,key=lambda x:x[1])
    club_ls=sorted(club_ls,key=lambda x:x[1])
    diamond_ls=sorted(diamond_ls,key=lambda x:x[1])
    
    return spade_ls+heart_ls+club_ls+diamond_ls


def find_miss_card():

    init_card_set=read_card()
    
    all_card=create_card_set()
    
    left_card=all_card - init_card_set
    
    result=sort_card(left_card)


    for ct,cn in result:
        print(f"{ct} {cn}")

find_miss_card()
