h, w = list(map(int, input().split()))


def France():
    """
    ABC
    ABC
    ABC
    """
    d, m = divmod(w, 3)
    if m == 0:
        return 0
    return h

def Germany():
    """
    AAA
    BBB
    CCC
    """
    d, m = divmod(h, 3)
    if m == 0:
        return 0
    return w

def Chile():
    """
    AB
    AB
    CC
    """
    hd, hm = divmod(h, 3)
    wd, wm = divmod(w, 2)
    found = w*h
    for i in range(2*hd, 2*hd+3):
        for j in range(wd, wd+3):
            A = i * j 
            B = i * (w - j)
            C = (h - i) * w
            D = max(A, B, C) - min(A, B, C)
            found = min(found, D)
    return found

def Madagascar():
    """
    ABB
    ACC
    """
    hd, hm = divmod(h, 2)
    wd, wm = divmod(w, 3)
    found = w*h
    for i in range(wd, wd+3):
        for j in range(hd, hd+3):
            A = i * h
            B = (w - i) * j
            C = (h - j) * (w - i)
            D = max(A, B, C) - min(A, B, C)
            found = min(found, D)
    return found

print(min(France(), Germany(), Chile(), Madagascar()))
