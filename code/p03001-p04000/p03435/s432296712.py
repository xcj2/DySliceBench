def main():
    """
    0 <= c <= 100
    c(i,j) = a(i) + b(j)
    a: 整数 -> 負もあるのでc特定の数不明

    c1,1 = a1 + b1
    c1,2 = a1 + b2
    c1,3 = a1 + b3

    c2,1 = a2 + b1
    c2,2 = a2 + b2
    c2,3 = a2 + b3

    c3,1 = a3 + b1
    c3,2 = a3 + b2
    c3,3 = a3 + b3

    a or b だけの式にできる
    →等しいか試す
    """
    N = 3
    C = [
        tuple(map(int, input().split()))
        for _ in range(N)
    ]

    editorial(C, N)


def editorial(C, N):
    a = [None] * N
    b = [None] * N

    a[0] = 0
    for i in range(N):
        # c - a[0]だけど0なので省略
        b[i] = C[0][i]
    for i in range(N):
        a[i] = C[i][0] - b[0]

    for i in range(N):
        for j in range(N):
            if C[i][j] != a[i] + b[j]:
                print("No")
                return

    print("Yes")


def editorial2(C, N):
    """
    3 x 3:
    abc
    def
    ghi

    a+e=b+d => (a1+b1)+(a2+b2)=(a1+b2)+(a2+b1)
    b+f=c+e
    d+h=e+g
    e+i=f+h

    2 x 2のgridをつくり、その対角要素の和/逆対角要素の和が等しい
    """
    pass


def AC(C, N):
    a = is_valid_a(C, N)
    if not a:
        print("No")
        return

    b = is_valid_b(C, N)
    if not b:
        print("No")
        return

    print("Yes")


def is_valid_a(C, N):
    """
    c1,1 - c2,1: a1 - a2
    c1,2 - c2,2: a1 - a2
    c1,3 - c2,3: a1 - a2
    --------------
    ci,1 - c(i+1),1: ai - a(i+1)
    ci,2 - c(i+1),2: ai - a(i+1)
    ci,3 - c(i+1),3: ai - a(i+1)
    """
    from itertools import combinations
    for x, y in combinations([0, 1, 2], 2):
        valid = C[x][0] - C[y][0] == C[x][1] - C[y][1] == C[x][2] - C[y][2]
        if not valid:
            return False

    return True


def is_valid_b(C, N):
    """
    c1,1 - c1,2: b1 - b2
    c1,2 - c1,3: b2 - b3
    c1,3 - c1,1: b3 - b1
    --------------
    ci,1 - ci,2: b1 - b2
    ci,2 - ci,3: b2 - b3
    ci,3 - ci,1: b3 - b1
    """
    b1_m_b2 = set()
    b2_m_b3 = set()
    b3_m_b1 = set()
    for i in range(N):
        b1_m_b2.add(C[i][0] - C[i][1])
        b2_m_b3.add(C[i][1] - C[i][2])
        b3_m_b1.add(C[i][2] - C[i][0])

    return len(b1_m_b2) == 1 and len(b2_m_b3) == 1 and len(b3_m_b1) == 1


if __name__ == '__main__':
    main()
