def main():
    n, m, v, p = list(map(int, input().split()))
    a = sorted(list(map(int, input().split())))
    # print(a)

    def value(i):
        if i+p >= n:
            return True
        if a[n-p] > a[i]+m:
            return False
        b = list(reversed([a[i]+m-j for j in a[:i] + a[i+1:n]]))[p-1:]
        #print(b)
        if b[0] < 0:
            return False
        rest = v-n+len(b)
        if rest <= 0:
            return True
        #print(rest)

        c = [min(m, i) for i in b]
        d = [i for i in c][:-rest]
        e = [m-i for i in c][-rest:]
        #print(d, e)
        if sum(d) < sum(e):
            return False
        else:
            return True

    def b_search(a, b, value):
        while a+1 < b:
            med = (a+b)//2
            if value(med):
                b = med
            else:
                a = med+1
        if a == b:
            return a
        else:
            if value(a):
                return a
            else:
                return b

    #print(value(1))

    print(n-b_search(0, n-1, value))


main()