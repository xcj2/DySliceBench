import math
import string


def readints():
    return list(map(int, input().split()))


def nCr(n, r):
    return math.factorial(n)//(math.factorial(n-r)*math.factorial(r))


def has_duplicates2(seq):  # リストに重複した要素があるか判定（要素にリストがある場合）
    seen = []
    for item in seq:
        if not(item in seen):
            seen.append(item)
    return len(seq) != len(seen)


def divisor(n):
    divisor = []
    for i in range(1, n+1):
        if n % i == 0:
            divisor.append(i)
    return divisor


s = list(map(str, input()))
# print(s)
for i in range(-1, 2):
    #print(i, s[i])
    if s[i] == 'C':
        print('WA')
        exit()

for c in s[1:]:
    if c == 'A':
        print('WA')
        exit()


def cnt(s):
    a = 0
    for i in range(2, len(s)-1):
        # print(i, s[i])
        if s[i] == 'C':
            a += 1
    if a == 1:
        return True
    else:
        return False


def remove(s):
    s.remove('A')
    s.remove('C')
    return s


def func(s):
    if s[0] == 'A':
        pass
    else:
        return False
    if cnt(s):
        pass
    else:
        return False
    return True


if func(s):
    s = remove(s)
    aa = 0
    for i in range(len(s)):
        if s[i].islower():
            aa += 1
    if aa == len(s):
        print('AC')
        exit()
print('WA')
