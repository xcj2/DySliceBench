n = int(input())

def tobase4(num):
    ans = ''
    while num>0:
        ans += str(num%4)
        num //= 4
    return ans[::-1]

def check(s):
    if '1' in s and '2' in s and '3' in s and '0' not in s:
        return True
    return False

def conv(s):
    s = s.replace('2','5')
    s = s.replace('3','7')
    s = s.replace('1','3')
    return s

res = 0
for i in range(10**9):
    s = tobase4(i)
    if not check(s):
        continue
    s = conv(s)
    s = int(s)
    #print(s)
    if n < s:
        break
    #print(s)
    res += 1
print(res)
