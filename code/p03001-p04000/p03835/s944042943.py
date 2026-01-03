

def read_input():
    k, s = map(int, input().split())

    return k, s


def check_z(z, k):
    if z <= k:
        return z
    else:
        return -1


def check_yz(y, k):
    count = 0
    tempy = min(y, k)
    while tempy >= 0:
        if check_z(y - tempy, k) != -1:
            count += 1
        tempy -= 1
    return count

def check_xyz(x, k):
    count = 0
    tempx = min(x, k)
    while tempx >= 0:
        yc = check_yz(x - tempx, k)
        if yc != -1:
            count += yc
        tempx -= 1
    return count



def submit():
    k, s = read_input()

    print(check_xyz(s, k))

if __name__ == '__main__':
    submit()
