n, k = [int(v) for v in input().split()]
r, s, p = [int(v) for v in input().split()]
t = input()


def get(seq, i):
    if i < 0:
        return None
    if i >= len(seq):
        return None
    return seq[i]

def get_win(c):
    if c == 'r':
        return 'p'
    elif c == 's':
        return 'r'
    else: # 'p'
        return 's'

def get_score(c):
    if c == 'r':
        return r 
    elif c == 's':
        return s
    else: # 'p':
        return p

score = 0
seq = [None] * n
for i in range(n):

    ti = t[i]
    win = get_win(ti)
    prev = get(seq, i-k)
    if win != prev:
        score += get_score(win)
        seq[i] = win
        continue

    n = get(t, i+k)
    if n is None:
        seq[i] = ti
    else:
        if prev is None:
            seq[i] = list(set('rsp') - set(n))[0]
        else:
            seq[i] = list(set('rsp') - set(n) - set(prev))
        
print(score)