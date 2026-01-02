

def check(lst, n):
    i = 0
    j = 1

    while j < n:
        if lst[i] > lst[j]:
            return False
        i += 1
        j += 1

    return True


def swap(lst, i, j):
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp


def submit():
    n = int(input())
    plist = list(map(int, input().split()))

    if check(plist, n):
        print('YES')
        return

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            swap(plist, i, j)
            if check(plist, n):
                print('YES')
                return
            swap(plist, j, i)

    print('NO')


if __name__ == '__main__':
    submit()
