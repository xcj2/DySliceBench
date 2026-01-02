

def takeAllByX(z, w, xs):
    return abs(w - xs[-1])

def forceLastByX(z, w, xs):
    return abs(xs[-2] - xs[-1])

def forceLast2ByX(z, w, xs):
    return play2ByY(z, w, xs[-2:])


def takeAllByY(z, w, xs):
    return abs(z - xs[-1])

def forceLastByY(z, w, xs):
    return abs(xs[-2] - xs[-1])

def play2ByY(z, w, xs):
    ta = takeAllByY(z, w, xs)
    fl = forceLastByY(z, w, xs)
    return min(ta, fl)



if __name__ == "__main__":
    n, z, w = list(map(int, input().split()))
    xs = tuple(map(int, input().split()))
    i = len(xs)
    if i == 1:
        print(takeAllByX(z, w, xs))
    elif i == 2:
        print(max(takeAllByX(z, w, xs), forceLastByX(z, w, xs)))
    else:
        print(max(takeAllByX(z, w, xs), forceLastByX(z, w, xs), forceLast2ByX(z, w, xs)))



