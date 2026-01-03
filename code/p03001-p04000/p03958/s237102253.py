
def read():
    return int(input())

def reads(sep=None):
    return list(map(int, input().split(sep)))

def main():
    k, t = reads()
    a = [list(x) for x in list(enumerate(reads()))]
    n = -1
    c = 0
    while sum([x[1] for x in a]):
        a = sorted(a, key=lambda x:x[1], reverse=True)
        if a[0][0] != n:
            n = a[0][0]
            a[0][1] -= 1
        else:
            if len(a) == 1:
                c += 1
                a[0][1] -= 1
            elif 0 < a[1][1]:
                a[1][1] -= 1
                n = a[1][0]
            else:
                a[0][1] -= 1
                c += 1
    print(c)

main()
