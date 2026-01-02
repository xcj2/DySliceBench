import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    n, x, m = input_int_list()

    # 方針 循環するため、その循環を見つける。
    # 1.循環を探す
    A = []
    used = set([x])
    A.append(x)
    while True:
        a_next = ((A[-1])**2) % m
        if a_next in used:
            n_loop = a_next
            break
        A.append(a_next)
        used.add(a_next)
    # 2.ループの場所を探す
    start_ptr = A.index(n_loop)
    end_ptr = len(A) - 1
    loop_len = end_ptr - start_ptr + 1
    loop_sum = sum(A[start_ptr:])
    ans = 0
    rem = n - 1
    # 3.ループに入るまで分を足す
    if start_ptr < rem:
        ans += sum(A[:start_ptr])
        rem -= start_ptr
        if rem >= loop_len > 0:
            ans += loop_sum * (rem // loop_len)
        rem = rem % loop_len
        ans += sum(A[start_ptr:start_ptr + rem + 1])
        print(ans)
    else:
        ans = sum(A[:n])
        print(ans)
        return

    return


if __name__ == "__main__":
    main()
