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

N,K = nums()
print(len(str(base_cvt(N,K))))