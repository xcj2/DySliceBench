from itertools import repeat

import random

def bitcount(x):
	result = 0
	while x > 0:
		if x % 2 == 1: 
			result += 1

		x //= 2
	return result

ff = {}

def f(x):
	count = 0
	while x != 0:
		count += 1
		#print(x, bitcount(x))
		x = x % bitcount(x)	
	return count

def brute(s):
	chars = [char for char in s]

	result = []

	def flip(i):
		if chars[i] == '1':
			chars[i] = '0'
		else:
			chars[i] = '1'

	for i in range(len(s)):
		flip(i)
		x = int("".join(chars), 2)
		result.append(f(x))
		flip(i)

	return result

def solve(n, s):
	bc = s.count('1')

	x = 0
	pow = 1
	for bit in reversed(range(n)):
		if s[bit] == '1':
			x += pow
		pow *= 2


	mods1 = []
	mod1, mod2 = bc + 1, bc - 1
	mods2 = []

	#print(mod1, mod2)

	pow = 1
	mods1.append(pow % mod1)

	if mod2 != 0:
		mods2.append(pow % mod2)

	for bit in range(1, n):
		if mod1 != 0:
			mods1.append(2 * mods1[bit - 1] % mod1)
		if mod2 != 0:
			mods2.append(2 * mods2[bit - 1] % mod2)

	mods1 = list(reversed(mods1))
	mods2 = list(reversed(mods2))

	#print(mods1)
	#print(mods2)

	x_mod_1 = 0
	x_mod_2 = 0
	for bit in reversed(range(n)):
		if s[bit] == '1':		
			x_mod_1 = (x_mod_1 + mods1[bit]) % mod1
			if mod2 != 0:
				x_mod_2 = (x_mod_2 + mods2[bit]) % mod2

	#print(x_mod_1, x_mod_2)

	result = []

	for bit in reversed(range(n)):
		if s[bit] == '0':
			new_mod = (x_mod_1 + mods1[bit]) % mod1
			result.append(1 + f(new_mod))

		else:
			if mod2 == 0:
				result.append(0)
			else:				
				new_mod = (x_mod_2 - mods2[bit]) % mod2
				#print('new mod', new_mod)
				result.append(1 + f(new_mod))

	return list(reversed(result))


#n = 200000
n = int(input())
s = input()
#s = "".join(list(repeat('1', n)))

sol = solve(n, s)
for x in sol:
	print(x)

#print(brute(s))