import math
def sieve_of_erastosthenes(num):
    input_list = [0 if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 else 1 for i in range(num)]
    input_list[0] = input_list[1] = 0
    input_list[2] = input_list[3] = input_list[5] = 1
    sqrt = math.sqrt(num)
    for serial in range(3, num, 2):
        if serial >= sqrt:
            return input_list
        for s in range(serial ** 2, num, serial): 
            input_list[s] = 0
q = int(input())
l_list = []
r_list = []
for i in range(q):
    l, r = map(int, input().split())
    l_list.append(l)
    r_list.append(r)
minval = min(l_list)
maxval = max(r_list)
sieve = sieve_of_erastosthenes(maxval+1)
def is_prime(x):
    return sieve[x]
def is_like2017(x):
    return is_prime(x) * is_prime(int((x+1)/2))
like2017 = list(range(maxval+1))
for i in like2017:
    like2017[i] = is_like2017(i)

integral = like2017
for i in range(1, len(integral)):
    integral[i] = integral[i] + integral[i-1]
for l, r in zip(l_list, r_list):
    print(integral[r] - integral[l-1])