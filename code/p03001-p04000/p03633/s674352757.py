# -*- coding: utf-8 -*-

N = int(input())
T = [0]*N

for i in range(N):
	T[i] = int(input())


#a, bの最大公約数を求める
def gcd(a, b):
	r = max(a, b) % min(a, b)
	


	if (r == 0):
		return min(a, b)

	else:
		return gcd(r, min(a, b))


#a, bの最小公倍数を求める
def lcm(a, b):
	return a * b // gcd(a, b)



#リストTの全要素の最小公倍数を求める
def LCM(T):
	l = len(T)



	if(l == 1):
		return T[0]

	elif(l == 2):
		return lcm(T[0], T[1])



	T1, T2 = [], []

	for i in range(l // 2):
		T1.append(T[i])

	for j in range(l - l // 2):
		T2.append(T[j + l // 2])



	return lcm(LCM(T1), LCM(T2))



print(LCM(T))