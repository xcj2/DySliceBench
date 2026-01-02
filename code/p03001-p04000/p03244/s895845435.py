def sortcounts(c: dict):
    a = [(v, k) for k, v in c.items()]
    return sorted(a, reverse=True)


def solve(a):
    m = len(a)//2

    o = [a[i] for i in range(len(a)) if i%2==0]
    e = [a[i] for i in range(len(a)) if i%2==1]

    # print(o)
    # print(e)

    import collections
    co = sortcounts(collections.Counter(o))
    ce = sortcounts(collections.Counter(e))

    # print(co)
    # print(ce)

    no, vo = co[0]
    ne, ve = ce[0]

    if vo != ve:
        ans = (m-no) + (m-ne)
    else:
        anse = (m-no) + m-(0 if len(co)<2 else co[1][0])
        anso = (m-ne) + m-(0 if len(ce)<2 else ce[1][0])
        ans = min(anse, anso)

    return ans


def main():
    _=input()
    a = list(map(int, input().split()))
    print(solve(a))


if __name__ == '__main__':
    main()




