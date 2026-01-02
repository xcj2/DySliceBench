
#最大公約数
def gcd(a,b):
    while b != 0:
        a, b = b, a%b
    return a
    # print(gcd(a,b))

#最小公倍数
def lcm(a,b):
    return a*b // gcd(a,b)
    # print(lcm(a,b))

def main():
    A, B, C, D = list(map(int, input().split()))

    count_c = B // C
    count_d = B // D
    count_union = B // lcm(C, D)

    total1 = B - count_c - count_d + count_union

    count_c = (A - 1) // C
    count_d = (A - 1) // D
    count_union = (A - 1) // lcm(C, D)

    total2 = A - 1 - count_c - count_d + count_union

    print(total1 - total2)

if __name__ == '__main__':
    main()