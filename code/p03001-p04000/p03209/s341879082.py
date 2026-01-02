def height(level):
    hei = 1
    for i in range(level):
        hei = 3 + 2 * hei
    return hei

def patty(level):
    pat = 1
    for i in range(level):
        pat = 1 + 2 * pat
    return pat

def ans(level, under):
    if under == 1:
        if level == 0:
            return 1
        else:
            return 0
    elif under <= 1 + height(level - 1):
        return ans(level - 1, under - 1)
    elif under == 2 + height(level - 1):
        return 1 + patty(level - 1)
    elif under <= 2 + 2 * height(level - 1):
        return 1 + patty(level - 1) + ans(level - 1, under - 2 - height(level - 1))
    else:
        return 1 + 2 * patty(level - 1)
    
n, x = map(int, input().split())
print(ans(n, x))

        