from math import *

def Prime_Factorization(M):
    factor_count_list = []
    root_M = int(sqrt(M))

    while root_M > 1:
        root_M = int(sqrt(M))

        for i in range(2, root_M + 1):
            e = 0
            while M % i == 0:
                e += 1
                M = M // i
            if e > 0:
                factor_count_list.append(e)
                break
        else:
            break

    if M > root_M:
        factor_count_list.append(1)

    return factor_count_list

def comb(num_object, num_bar):
    numerator = 1

    for i in range(num_bar):
        numerator = (numerator * (num_object - i))

    return  numerator // factorial(num_bar)

def all_comb(N, factor_count_list):
    ans = 1
    for factor in factor_count_list:
        ans = (ans * comb(factor + N - 1, factor)) % (10 ** 9 + 7)
    return ans

def main():
    N, M = map(int, input().split())
    factor_count_list = Prime_Factorization(M)

    print(all_comb(N, factor_count_list))

if __name__ == "__main__":
    main()