import numpy as np

def check(number):
    string = str(number)
    if("3" in string and "5" in string and "7" in string):
        if(number <= N):
            return 1
    return 0

def make_root_three(num):
    ans = 0
    i = 0
    while(num // 3):
        ans += (num % 3) * (10 ** i)
        num = num // 3
        i += 1
    ans += num * (10 ** i)
    return ans

def make_number_from_seed(seed, l):
    ans = 0
    string = str(seed).zfill(l)
    for i in range(l):
        ans += candidates[int(string[i])] * (10 ** i)
    return ans

N = int(input().strip())
length = int(np.log10(N)) + 1

candidates = [3, 5, 7]
ans = 0

for l in range(3, length + 1):
    for i in range(3**l):
        seed = make_root_three(i)
        number = make_number_from_seed(seed, l)
        ans += check(number)
    
print(ans)