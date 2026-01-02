def count_inv(lst):
    ret = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                ret += 1
    return ret


def count_smaller_elements(lst):
    ret = 0
    for i in range(len(lst)):
        tmp = 0
        for j in range(len(lst)):
            if i != j and lst[i] > lst[j]:
                tmp += 1
        ret += tmp
    return ret


def main():
    N, K = map(int, input().split())
    lst_A = list(map(int, input().split()))
    MOD = 10 ** 9 + 7

    a = count_inv(lst_A)
    num1 = a * K % MOD

    b = count_smaller_elements(lst_A)
    num2 = b * (K * (K - 1) // 2) % MOD

    ans = (num1 + num2) % MOD
    print(ans)


if __name__ == "__main__":
    main()