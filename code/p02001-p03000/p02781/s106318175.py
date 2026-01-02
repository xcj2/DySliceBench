n = int(input())
k = int(input())
import math
def k1(n):
    if n < 10:
        ans = n
    else:
        n1 = str(n)
        n2 = int(n1[0])
        ans = 9 * (len(n1) - 1) + n2
    return int(ans)

def k2(n):
    if n < 100:
        ans = n - k1(n)
    else:
        n1 = str(n)
        n2 = int(n1[0])
        ans = (81 * (math.factorial(len(n1) - 1) / math.factorial(len(n1) - 3)) / 2) +  (n2 - 1) * k1(10 ** (len(n1) - 1) - 1) + k1(n - n2 * 10 ** (len(n1) - 1))
    return int(ans)

def k3(n):
    if n < 1000:
        ans = n - k2(n) - k1(n)
    else:
        n1 = str(n)
        n2 = int(n1[0])
        ans = (729 * (math.factorial(len(n1) - 1) / math.factorial(len(n1) - 4)) / 6) + (n2 - 1) * k2(10 ** (len(n1) - 1) - 1) + k2(n - n2 * 10 ** (len(n1) - 1))
    return int(ans)

if k == 1:
    print(k1(n))
elif k == 2:
    print(k2(n))
else:
    print(k3(n))