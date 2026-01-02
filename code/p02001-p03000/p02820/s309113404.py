def win(hand):
        if hand == 'r':
            return 'p'
        elif hand == 'p':
            return 's'
        else:
            return 'r'

def get_best_hand(hand, last_hand):
    won_hand = win(hand)
    if won_hand == last_hand:
        return 'draw'
    else:
        return won_hand
    
def get_point(hand, R, S, P):
        if hand == 'r':
            return R
        elif hand == 'p':
            return P
        elif hand == 's':
            return S
        else:
            return 0

K = int(input().split()[1])
R, S, P = map(int, input().split())
T = input()

last_hand = ''
history = []
point = 0

for t in T:
    last_hand = history[0] if len(history) >= K else ''
    best_hand = get_best_hand(t, last_hand)
    point += get_point(best_hand, R, S, P)
    history.append(best_hand)
    if len(history) > K:
        del history[0]

print(point)