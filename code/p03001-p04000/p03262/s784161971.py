#最大公約数
def gcd(a, b):
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return b

#最小公倍数
def lcm(a, b):
    return a * b // gcd(a, b)

#最大公約数（複数）
def gcds(l):
    if len(l) == 1:
        return l[0]
    elif len(l) == 2:
        return gcd(l[0], l[1])
    else:
        n = len(l) // 2
        L = l[:n]
        R = l[n:]
        return gcd(gcds(L), gcds(R))

#最小公倍数(複数)
def lcms(l):
	if len(l) == 1:
		return l[0]
	elif len(l) == 2:
		return lcm(l[0], l[1])
	else:
		n = len(l) // 2
		L = l[:n]
		R = l[n:]
		return lcm(lcms(L), lcms(R))
      
n, X = (int(i) for i in input().split())  
x = [int(i) for i in input().split()] 
x.append(X)
mm = min(x)
x.remove(mm)
#print(x)
for i in range(n):
  x[i] -= mm
#print(x)
print(gcds(x))