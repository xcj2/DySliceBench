

def read_input():
    n = int(input())
    alist = list(map(int, input().split()))

    return n, alist


def possibility_check(n, alist):
    alist.sort()

    if n % 2:
        even = [x for x in range(2, n) if x % 2 == 0]
        comp = [0] + even + even
        comp.sort()

    else:
        odd = [x for x in range(1, n) if x % 2 == 1]
        comp = odd + odd
        comp.sort()

    if alist == comp:
        return True
    else:
        return False


def submit():
    n, alist = read_input()

    if possibility_check(n, alist):
        # ans = (2 ** (n // 2)) % (10**9 + 7)
        ans = 1
        for i in range(n // 2):
            ans *= 2
            if ans > 10**9 + 7:
                ans %= (10**9 + 7)
        print(ans)
    else:
        print(0)


if __name__ == '__main__':
    submit()
