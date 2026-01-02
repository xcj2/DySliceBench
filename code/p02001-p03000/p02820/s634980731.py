def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = list(input())
    sub_ts = [[] for i in range(K)]
    for index, t in enumerate(T):
        sub_ts[index % K].append(t)

    total = 0
    for sub_t in sub_ts:
        total += sub(sub_t, R, S, P)
    print(total)

def sub(T, R, S, P):
    point = 0
    last_te = None
    for t in T:
        if last_te is None or can_win(last_te, t):
            te, p = win(t, R, S, P)
            last_te = te
            point += p
        else:
            last_te = 'o'
    return point

def win(enemy_t, R, S, P):
    if enemy_t == 'r':
        return 'p', P
    elif enemy_t == 's':
        return 'r', R
    else:
        return 's', S

def can_win(last_te, enemy_t):
    win_t = None
    if enemy_t == 'r':
        win_t = 'p'
    elif enemy_t == 's':
        win_t = 'r'
    else:
        win_t = 's'
    return last_te != win_t

main()
