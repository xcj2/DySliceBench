N = int(input())

def count_digit(n):
    cnt = 1
    while True:
        n = n // 10
        if n == 0:
            break
        else:
            cnt += 1
    return cnt

def gcd(x,y):
    if x%y==0:
        return y
    else:
        return gcd(y, x%y)

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        # nを合う数字で割り切れたら、その割った数と商をリストに追加する。
        # nが平方数のとき、同じ数字が2回追加されてしまうので3行したのif文がある
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

divs_list = make_divisors(N)

min_f = 12
len_d = len(divs_list)
for i in range(len_d):
    if i > len_d-i:
        break
    cnt = max(count_digit(divs_list[i]),count_digit(divs_list[len_d-i-1]))
    if min_f > cnt:
        min_f = cnt
print(cnt)