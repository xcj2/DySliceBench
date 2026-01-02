def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    del divisors[0]
    return divisors

def check_mod(n, k):
    if k == 1:
        return False
    while n != 0:
        mod = n % k
        if mod == 0:
            n = n/k
        elif mod == 1:
            return True
        else:
            return False

def main():
    n = int(input())
    #あまりが1のやつ
    res = len(make_divisors(n-1))

    for dv in make_divisors(n):
        if check_mod(n, dv):
            res += 1
    print(res)

if __name__ == '__main__':
    main()

