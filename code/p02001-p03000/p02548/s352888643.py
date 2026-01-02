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

def main():
    N = int(input())
    ans = 1
    for c in range(2, N):
        p = factorization_counta(c)
        tmp = 1
        for v in p:
            tmp *= (v + 1)
        ans += tmp
    return ans
 
if __name__ == '__main__':
    print(main())