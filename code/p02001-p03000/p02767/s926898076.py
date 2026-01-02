def num():
    return int(input())
def nums():
    return list(map(int,input().split()))
import string
numbers = "0123456789"
alphabets = string.ascii_letters # a-z+A-Zをロード
characters = numbers + alphabets
 
def base_cvt(value, n=2):
    try:
        tmp = int(value)
    except:
        raise ValueError('Invalid value:', value)
 
    if n < 2 or n > len(characters):
        raise ValueError('Invalid n:', value)
 
    result = ''
    tmp = int(value)
    while tmp >= n:
        idx = tmp%n
        result = characters[idx] + result
        tmp = int(tmp / n)
    idx = tmp%n
    result = characters[idx] + result
    return result

N = num()
X = nums()
def get_cost(l,pos):
    cost = 0
    for xi in l:
        cost += (xi - pos)**2
    return cost
costs = set()
for i in range(min(X)-1,max(X)+1):
    costs.add(get_cost(X,i))
print(min(costs))