def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

A,B = map(int,input().split())

def count_(upper_num):
    data = [2] + list(range(3,upper_num+1,2))
    idx = 0
    length = len(data)
    while idx < length:
        prime = data[idx]
        data = [d for d in data if (d==prime or d % prime != 0)]
        idx += 1
        length = len(data)
    
    return data

def make_divisors(n):
    divisors = [1]
    i = 2 
    max_int = int(n**0.5)+1
    while n >1:
#         print(n)
        if i >= max_int:
#             print("max")
            divisors.append(n)
            break
        # nを合う数字で割り切れたら、その割った数と商をリストに追加する。
        # nが平方数のとき、同じ数字が2回追加されてしまうので3行したのif文がある
        if n % i == 0:
            divisors.append(i)
            max_int = int((n//i)**0.5)+1
            while n%i == 0:
                n = n//i
                
        i += 1

    divisors = list(set(divisors))
#     divisors.sort()
    return divisors

print(len(make_divisors(gcd(A,B))))