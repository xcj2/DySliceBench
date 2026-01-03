
def read_input():
    n = int(input())
    alist = list(map(int, input().split()))
    return n, alist

def get_sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0

def submit():
    n, alist = read_input()

    # pattern 1
    s = 0
    sign = 1
    edit = 0

    for a in alist:
        temp = s + a
        temp_sign = get_sign(temp)

        if sign == temp_sign:
            edit += temp_sign * temp
            temp -= temp

        if temp == 0:
            edit += 1
            temp -= sign

        s = temp
        sign = get_sign(s)

    edit1 = edit

    # pattern 2
    s = 0
    sign = -1
    edit = 0

    for a in alist:
        temp = s + a
        temp_sign = get_sign(temp)

        if sign == temp_sign:
            edit += temp_sign * temp
            temp -= temp

        if temp == 0:
            edit += 1
            temp -= sign

        s = temp
        sign = get_sign(s)

    edit2 = edit

    print(min(edit1, edit2))


if __name__ == '__main__':
    submit()
    