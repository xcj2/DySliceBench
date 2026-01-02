def make_divisor_list(num): # 約数を求める
    if num < 1:
        return []
    elif num == 1:
        return [1]
    else:
        divisor_list = []
        i = 1
        while i*i <= num:
            if num%i == 0:
                divisor_list.append(i)
                divisor_list.append(num//i)

            i += 1
        divisor_list.append(num)

        return sorted(set(divisor_list))

def factorial(n): # 階乗を求める
    if n == 0 or n == 1:
        return 1
    else:
        ans = n*factorial(n-1)

        return ans
def usage(n):

    fct = factorize(n)
    return fct

def factorize(n):
    fct = []  # prime factor
    b, e = 2, 0  # base, exponent
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct

def num(fct):
    a = 1
    for base, exponent in fct:
        a = a * base**exponent
    return a

N = int(input())

NN = factorial(N)
usa = usage(NN)

ans = 0
div_75 = [3, 5, 15, 25, 75]


nums = [0 for _ in range(75+1)]

for i in usa:
    for divs in div_75:
        if i[1] >= divs-1:
            nums[divs] = nums[divs] + 1

ans = 0

if nums[5] >= 2:
    num_tmp = nums[5]
    tmp = factorial(num_tmp)//(2*factorial(num_tmp-2))
    ans += (nums[3] - 2) * tmp

if nums[15] >= 1:
    num_tmp = nums[15]
    tmp = num_tmp
    ans += (nums[5] - 1) * tmp

if nums[25] >= 1:
    tmp = nums[25]
    ans += (nums[3] - 1) * tmp

if nums[75] >= 1:
    ans += nums[75]


print(ans)
