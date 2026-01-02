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

N,K = map(int,input().split())
a_list = list(map(int,input().split()))

sums = sum(a_list)
divisors = make_divisors(sums)
divisors.reverse()

def func():
    for d in divisors:
        amaris = [a%d for a in a_list]
        amaris.sort()
        amaris.reverse()
        amari_sum = sum(amaris)
        hanten_cnt = int(amari_sum / d)
        sousa_cnt = 0
        for i in range(hanten_cnt):
            sousa_cnt += d - amaris[i]
        if sousa_cnt <= K:
            return d

result = func()

print(result)