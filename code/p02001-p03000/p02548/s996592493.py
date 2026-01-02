def get_sieve_of_eratosthenes(n):
    if not isinstance(n, int):
        raise TypeError("n is int-type.")
    if n < 2:
        raise ValueError("n is more than 2")
    data = [i for i in range(2, n + 1)]
    for d in data:
        data = [x for x in data if (x == d or x % d != 0)]
    return data

p_list = get_sieve_of_eratosthenes(10**3)

def factorization_counta(n):
    arr = []
    temp = n
    for i in p_list:
        if i * i > n:
            break
        elif temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append(cnt)
            
    if temp != 1:
        arr.append(1)
    if arr == []:
        arr.append(1)
    return arr

def get_number_comb(arr):
    ans = 1
    for i in arr:
        ans *= (i + 1)
    return ans

# 約数の数 == その数に掛け算でなるための組み合わせの数

def main(N):
    ans = 1
    for n in range(2, N):
        ans += get_number_comb(factorization_counta(n))
    print(ans)


if __name__ == '__main__':
    N = int(input())
    main(N)