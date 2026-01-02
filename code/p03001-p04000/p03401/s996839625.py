def is_a_mid(a, b, c):
    return (b <= a <= c) or (c <= a <= b)


def is_b_mid(a, b, c):
    return (a <= b <= c) or (c <= b <= a)


def solve(n, a):
    total = 0
    ans = []

    for i, j in zip(a, a[1:]):
        total += abs(j-i)

    for i, j, k in zip(a, a[1:], a[2:]):
        if is_a_mid(i, j, k):
            ans.append(total-2*(abs(j-i)))
        elif is_b_mid(i, j, k):
            ans.append(total)
        else:
            ans.append(total+abs(i-k) - abs(i-j) - abs(k-j))

    return ans


if __name__ == '__main__':
    n = int(input())
    a = [0] + list(map(int, input().split()))+[0]
    for i in solve(n, a):
        print(i)
