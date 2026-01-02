import math

def extgcd(a,b):
    r = [1,0,a]
    w = [0,1,b]
    while w[2]!=1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2
    #[x,y]
    return [w[0],w[1]]

def mod_inv(a,m):
    x = extgcd(a,m)[0]
    return (m+x%m)%m

mod = 10 ** 9 + 7
x, y = list(map(int, input().split()))

def mod_fact(frm, to):
	ans = 1
	for i in range(frm, to + 1):
		ans = (ans * i) % mod
	return ans



if (x + y) % 3 == 0 and x <= y * 2 and y <= x * 2:
	n = (y * 2 - x) // 3
	m = (x + y) // 3
	#print(n, m)
	#print(mod_fact(m - n + 1, m))
	#print(mod_fact(1, n))

	print((mod_fact(m - n + 1, m) * (mod_inv(mod_fact(1, n), mod)) % mod))
else:
	print(0)
