def patty_num(N):
    if N == 0:
        return 1
    return 1 + 2 * patty_num(N - 1)

def burger_height(N):
    if N == 0:
        return 1
    else:
        return 3 + 2 * burger_height(N - 1)
    
def f(N, X):
    if X == 1:
        if N == 0:
            return 1
        else:
            return 0
    elif 1 < X and X <= burger_height(N - 1) + 1:
        return f(N - 1, X - 1)
    elif X == burger_height(N - 1) + 2:
        return patty_num(N - 1) + 1
    elif burger_height(N - 1) + 2 < X and X <= 2 * burger_height(N - 1) + 2:
        return patty_num(N - 1) + 1 + f(N - 1, X - 2 - burger_height(N - 1))
    
    return 2 * patty_num(N - 1) + 1
    
N, X = map(int, input().split())
print(f(N, X))
    