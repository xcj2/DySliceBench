n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()

scores = {'r':r,'p':p,'s':s}
def calc_score(my_hand, other_hand):
    if my_hand == 'r' and other_hand == 's':
        return r
    elif my_hand == 's' and other_hand == 'p':
        return s
    elif my_hand == 'p' and other_hand == 'r':
        return p
    else:
        return 0

def winnable_hand(other_hand):
    if other_hand == "r":
        return "p"
    elif other_hand == "p":
        return "s"
    else:
        return "r"
def losable_hand(other_hand):
    if other_hand == "r":
        return "s"
    elif other_hand == "p":
        return "r"
    else:
        return "p"

result = 0
for i in range(k):
    target = t[i::k]
    rps = {'r':0,'p':0,'s':0}
    for other_hand in target:
        wh = winnable_hand(other_hand)
        lh = losable_hand(other_hand)
        r_max = max(rps['p'], rps['s'])
        p_max = max(rps['r'], rps['s'])
        s_max = max(rps['p'], rps['r'])
        current_max = {hand: m for hand, m in zip(["r","s","p"], [r_max, s_max, p_max])}
        rps[wh] = current_max[wh] + scores[wh]
        rps[other_hand] = current_max[other_hand]
        rps[lh] = current_max[lh]
    
    result += max(rps.values())

print(result)
