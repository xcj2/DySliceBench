def print_func(s, order):
    print(s[order[1]:order[2]+1])


def reverse_func(s, order):
    ans = list(s[order[1]:order[2]+1])
    ans.reverse()
    s = s[:order[1]]+''.join(ans)+s[order[2]+1:]
    return s


def replace_func(s, order):
    cnt = 0
    s = list(s)
    for i in range(order[1], order[2]+1):
        s[i] = str(order[3])[cnt]
        cnt += 1
    s = ''.join(s)
    return s


if __name__ == '__main__':
    s = input()
    for i in range(int(input())):
        order = input().split()
        order[1] = int(order[1])
        order[2] = int(order[2])
        if order[0] == 'print':
            print_func(s, order)
        elif order[0] == 'reverse':
            s = reverse_func(s, order)
        else:
            s = replace_func(s, order)