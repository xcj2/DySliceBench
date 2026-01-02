def burger_size(N):
    if N == 0:
        return 1
    return 3 + 2 * burger_size(N - 1)

def burger_patty_num(N):
    if N == 0:
        return 1
    return 1+ 2 * burger_patty_num(N - 1)

def patty_num(N, X):
    if X == 0:
        return 0
    if N == 0:
        return 1
    if X <= 1 + burger_size(N - 1):
        return patty_num(N - 1, X - 1)
    elif X == 2 + burger_size(N - 1):
        return 1 + burger_patty_num(N - 1)
    elif X <= 2 + 2 * burger_size(N - 1):
        return 1 + burger_patty_num(N - 1) + patty_num(N - 1, X - (2 + burger_size(N - 1)))
    else:
        return 1 + 2 * burger_patty_num(N - 1)
        
    
N, X = map(int, input().split())
print(patty_num(N, X))