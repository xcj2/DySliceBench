import bisect
import math
n = int(input())
if n == 1:
    print(0)
    exit()

def get_primenumber(N):
    #素数リスト
    prime_list = [2]
    #3からNまでの数字を一つずつ取り出す
    for num in range(3,N+1,2):
      #取り出した数字が素数リストの要素で割れなければ素数リストに追加する
      if all( num % prime != 0 for prime in prime_list):
        prime_list.append(num)

    return prime_list

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

sosuu = get_primenumber(100)

sosuu_list = [0] * len(sosuu)

for i in range(2, n+1):
    a = factorization(i)
    for j in a:
        index = bisect.bisect_left(sosuu, j[0])
        sosuu_list[index] += j[1]
    over_74 = len([x for x in sosuu_list if x >= 74])
    over_24 = len([x for x in sosuu_list if x >= 24])
    over_14 = len([x for x in sosuu_list if x >= 14])
    over_4  = len([x for x in sosuu_list if x >= 4])
    over_2  = len([x for x in sosuu_list if x >= 2])
    ans = over_74 + over_24 * (over_2 - 1) + over_14 * (over_4 - 1)
    if over_4 >= 2:
        ans += combinations_count(over_4, 2) * max(0, (over_2 - 2))

print(ans)