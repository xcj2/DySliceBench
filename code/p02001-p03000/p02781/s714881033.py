def K1(n):
    ans = 0
    d = len(str(n))
    ans += int(str(n)[0])
    ans += 9 * (d-1)
    return ans


def K2(n):
    d = len(str(n))
    ans = 9**2*(d-2)*(d-1)//2
    ans += (int(str(n)[0]) - 1) * 9 * (d-1)
    ans += K1(int(str(n)[1:]))
    return ans


def K3(n):
    d = len(str(n))
    ans = 0
    for i in range(2,d-1):
        ans += i*(i-1)//2
    ans *= 9**3
    ans += (int(str(n)[0]) - 1) * 9**2 * (d-1)*(d-2) // 2
    ans += K2(int(str(n)[1:]))
    return ans


def main():
    N = int(input())
    K = int(input())

    if K == 1:
        print(K1(N))

    if K == 2:
        if N < 10:
            print(0)
            exit()
        print(K2(N))

    if K == 3:
        if N < 100:
            print(0)
            exit()
        print(K3(N))



if __name__ == "__main__":
    main()
