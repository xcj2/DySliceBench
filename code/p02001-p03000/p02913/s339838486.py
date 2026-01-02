def cin():  return list(map(int,input().split()))

def alpha2num(alpha):
    num = 0
    for index, item in enumerate(list(alpha)):  num += pow(26, len(alpha) - index - 1) * (ord(item) - ord('a') + 1)
    return num

def rol_hash(l):

    b, h = 1007, 10 ** 9 + 9
    base = pow(b, l, h)
    hash_s = 0
    dic = {}
    for i in range(l):  hash_s = (hash_s * b + alpha2num(S[i])) % h
    dic[hash_s] = l - 1
    for i in range(1, N - l + 1):
        hash_s = (hash_s * b - base * alpha2num(S[i - 1]) + alpha2num(S[i + l - 1])) % h
        if hash_s in dic:
            if S[dic[hash_s] - l + 1:dic[hash_s] + 1] == S[i:i + l] and dic[hash_s] < i:  return 1
        else:  dic[hash_s] = i + l - 1
    return 0

def is_ok(mid):  return rol_hash(mid)

def binary_search(left, right):
    while (abs(right - left) > 1):
        mid = (left + right) // 2
        if is_ok(mid):  right = mid
        else:  left = mid
    return right

N = cin()[0]
S = input()

left = N + 1
right = -1
ret = binary_search(left, right)
if ret == right:  print(0)
else:  print(ret)