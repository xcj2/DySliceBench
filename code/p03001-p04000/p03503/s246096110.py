
def read_input():
    n = int(input())

    flist = []
    for i in range(n):
        flist.append(list(map(int, input().split())))

    plist = []
    for j in range(n):
        plist.append(list(map(int, input().split())))

    return n, flist, plist


# aとbの1が重複している数を数える
def check_open(a, b):
    c = 0
    for i,j in zip(a, b):
        if i == j == 1:
            c += 1

    return c

# 整数を受け取り、2進数のリストにして返す
def get_pattern(p):
    binary_p = bin(p)[2:]
    list_p = [int(c) for c in binary_p]
    list_p = [0]*(10 - len(list_p)) + list_p
    return list_p


def submit():
    n, flist, plist = read_input()
    max_pattern = 2048
    max_profit = -float('inf')
    for p in range(1, 2048):
        myshop = get_pattern(p)
        profit = 0
        for i in range(n):
            target_shop = flist[i]
            c = check_open(myshop, target_shop)
            profit += plist[i][c]

        if max_profit < profit:
            max_profit = profit

    print(max_profit)

if __name__ == '__main__':
    submit()