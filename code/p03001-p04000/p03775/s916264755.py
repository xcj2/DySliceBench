def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


def factorize_list_format_change(fact_list_old):
    fact_list_new = []
    for prime_num in fact_list_old:
        for _ in range(prime_num[1]):
            fact_list_new.append(prime_num[0])
    return fact_list_new


def calc_degit(num):
    return len(str(num))

def solve():
    N = int(input())
    fact_list_old = factorization(N)
    fact_list = factorize_list_format_change(fact_list_old)
    min_F = calc_degit(N)
    for i in range(1, 2**len(fact_list)):
        A = 1
        B = 1
        grouping_str = format(i, '0'+str(len(fact_list))+'b')
        for j in range(len(fact_list)):
            if grouping_str[j] == "0":
                A *= fact_list[j]
            else:
                B *= fact_list[j]
        min_F_temp = max(calc_degit(A), calc_degit(B))
        if(min_F_temp < min_F):
            min_F = min_F_temp
    print(min_F)


if __name__ == "__main__":
    solve()