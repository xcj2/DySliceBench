# ABC157e


#print(bin(toBitSet([1, 2, 3, 2])))

# for i in range(97, 123):
#    print(chr(i))


def main():
    import sys
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    #####segfunc######
    def segfunc(x, y):
        return x | y  # 例としてmin関数を設定

    def init(init_val):  # セグ木にしたい配列を渡す
        # set_val
        for i in range(len(init_val)):
            seg[i+num-1] = init_val[i]
        # built
        for i in range(num-2, -1, -1):
            seg[i] = segfunc(seg[2*i+1], seg[2*i+2])

    def update(k, x):
        k += num-1
        seg[k] = x
        while k:
            k = (k-1)//2
            seg[k] = segfunc(seg[k*2+1], seg[k*2+2])

    def query(p, q):
        if q <= p:
            return ide_ele
        p += num-1
        q += num-2
        res = ide_ele
        while q-p > 1:
            if p & 1 == 0:
                res = segfunc(res, seg[p])
            if q & 1 == 1:
                res = segfunc(res, seg[q])
                q -= 1
            p = p//2
            q = (q-1)//2
        if p == q:
            res = segfunc(res, seg[p])
        else:
            res = segfunc(segfunc(res, seg[p]), seg[q])
        return res

    #####単位元######
    ide_ele = 0

    n = int(input())
    s = list(input())
    q = int(input())
    # num:n以上の最小の2のべき乗
    num = 2**(n-1).bit_length()  # nは元々の配列の長さ
    seg = [ide_ele] * (2 * num+1)

    def toBitSet(numberSet):
        theSet = 0
        for i in numberSet:
            theSet = theSet | 1 << i
        return theSet

    def alphabetToZeroIndexed(alphabet):
        return ord(alphabet)-97

    for i in range(n):
        update(i+1, toBitSet([alphabetToZeroIndexed(s[i])]))

    for _ in range(q):
        a, b, c = input().split()
        b = int(b)
        if int(a) == 1:
            update(b, toBitSet([alphabetToZeroIndexed(c)]))
        else:
            c = int(c)
            print(bin(query(b, c+1)).count('1'))


if __name__ == '__main__':
    main()
