

def read_input():
    n = int(input())
    xlist = list(map(int, input().split()))
    return n, xlist


def get_median(s, ignore):
    l = len(s)
    if ignore < l/2:
        return s[int((l+1)/2)]
    else:
        return s[int((l-1)/2)]

def submit():
    n, xlist = read_input()

    xlist = [(x, i) for i, x in enumerate(xlist)]
    xlist.sort(key=lambda x: x[0])

    pos_dic = {}
    for i, x in enumerate(xlist):
        pos_dic[x[1]] = i

    for i in range(n):
        target = pos_dic[i]
        print(get_median(xlist, target)[0])




if __name__ == '__main__':
    submit()
