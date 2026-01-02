level, num_eat = map(int,input().split())

def get_layers(level):
    return 2**(level+2) - 3

def get_patty(level):
    return 2**(level+1) - 1

def f(level, x):
    if level == 0:
        return 1
    elif x == 1:
        return 0
    elif 1 < x <= 1 + get_layers(level-1):
        return f(level-1, x-1)
    elif x == 2 + get_layers(level-1):
        return get_patty(level - 1) + 1
    elif 2 + get_layers(level-1) < x <= 2 + 2 * get_layers(level-1):
        return get_patty(level-1) + 1 + f(level-1,x-2-get_layers(level-1))
    elif x == 3 + 2*get_layers(level-1):
        return 2*get_patty(level - 1) + 1

print(f(level, num_eat))