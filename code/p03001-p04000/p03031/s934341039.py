

def read_input():
    n, m = map(int, input().split())

    slist = []
    for i in range(m):
        temp = list(map(int, input().split()))
        k = temp[0]
        s = temp[1:]
        slist.append((k, s))

    p = list(map(int, input().split()))

    return n, m, slist, p


def switch_gen(n):
    curr = 0

    while True:
        bincurr = bin(curr)[2:]

        if len(bincurr) > n:
            return None
        bincurr = [int(c) for c in bincurr]
        t = [0] * (n - len(bincurr))
        t.extend(bincurr)
        yield t

        curr += 1


def check_condition(switch, slist, plist):
    for s, p in zip(slist, plist):
        count = 0
        for i in s[1]:
            if switch[i - 1] == 1:
                count += 1

        if count % 2 != p:
            return False

    return True


def submit():
    n, m, slist, p = read_input()

    count = 0
    for switch in switch_gen(n):
        if check_condition(switch, slist, p):
            count += 1

    print(count)




if __name__ == '__main__':
    submit()
