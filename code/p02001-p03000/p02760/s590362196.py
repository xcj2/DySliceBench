card = [[list(map(int, input().split())) for _ in range(3)],
        [[0 for _ in range(3)] for _ in range(3)]]
N = int(input())
B = [int(input()) for _ in range(N)]

sc = 1
DEB = False

def check_vertical(card):
    V = [sum(card[sc][i]) for i in range(3)]
    if DEB: print(V)
    return (3 in V)

def check_horizen(card):
    H = [sum([card[sc][j][i] for j in range(3)]) for i in range(3)]
    if DEB: print(H)
    return (3 in H)
def check_diag(card):
    D = [card[sc][0][0]+card[sc][1][1]+card[sc][2][2],
         card[sc][0][2]+card[sc][1][1]+card[sc][2][0]]
    if DEB: print(D)
    return(3 in D)

def check_card(card):
    return (check_diag(card) or check_horizen(card) or check_vertical(card))

for b in B:
    for i in range(3):
        for j in range(3):
            if card[0][i][j] == b: card[1][i][j] = 1
            tf = check_card(card)
            if tf:
                print('Yes')
                break
        else:
            continue
        break
    else:
        continue
    break
else:
    if tf is False:
        print('No')