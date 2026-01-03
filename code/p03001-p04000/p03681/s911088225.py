import sys

MOD = 10 ** 9 + 7
MOD = 10 ** 9 + 7
class ModInt:

	def __init__(self, x, inv=None):
		self.x = x.x if isinstance(x, ModInt) else x % MOD
		self.inv = inv

	__str__ = lambda self:str(self.x)
	__repr__ = __str__
	__int__ = lambda self: self.x
	__index__ = __int__

	__add__ = lambda self, other: ModInt(self.x + ModInt(other).x)
	__radd__ = lambda self, other: ModInt(other + self.x)
	__iadd__ = __add__

	__sub__ = lambda self, other: ModInt(self.x - ModInt(other).x)
	__rsub__ = lambda self, other: ModInt(other - self.x)
	__isub__ = __sub__

	__mul__ = lambda self, other: ModInt(self.x * ModInt(other).x)
	__rmul__ = lambda self, other: ModInt(other * self.x)
	__imul__ = __mul__

	__pow__ = lambda self, other: ModInt(pow(self.x, ModInt(other).x, MOD))
	__rpow__ = lambda self, other: ModInt(pow(other, self.x, MOD))
	__pow__ = __pow__

	def __truediv__(self, other):
		if isinstance(other, ModInt) and other.inv != None:
			return ModInt(self.x * other.inv)
		else:
			return ModInt(self.x * pow(ModInt(other).x, MOD - 2, MOD))
	
	def __rtruediv__(self, other):
		if not self.inv:
			return ModInt(other * pow(self.x, MOD - 2, MOD))
		else:
			return ModInt(other * self.inv)

	__itruediv__ = __truediv__

	__floordiv__ = lambda self, other: ModInt(self.x // ModInt(other).x)
	__rfloordiv__ = lambda self, other: ModInt(other // self.x)
	__ifloordiv__ = __floordiv__

	__mod__ = lambda self, other: ModInt(self.x % other)
	__rmod__ = lambda self, other: ModInt(other % self.x)
	__imod__ = __mod__

	__lt__ = lambda self, other: self.x < ModInt(other).x
	__gt__ = lambda self, other: self.x > ModInt(other).x
	__le__ = lambda self, other: self.x <= ModInt(other).x
	__ge__ = lambda self, other: self.x >= ModInt(other).x
	__eq__ = lambda self, other: self.x == ModInt(other).x
	__ne__ = lambda self, other: self.x != ModInt(other).x


class Fact:
	def __init__(self, MAX):
		MAX += 1
		self.fact = [0] * MAX
		finv = [0] * MAX
		inv = [0] * MAX
		self.fact[0] = 1
		self.fact[1] = 1
		finv[0] = 1
		finv[1] = 1
		inv[1] = 1
		for i in range(2, MAX):
			self.fact[i] = self.fact[i - 1] * i % MOD
			inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
			finv[i] = finv[i - 1] * inv[i] % MOD
		for i in range(MAX):
			self.fact[i] = ModInt(self.fact[i], inv=finv[i])
	def __call__(self, value):
		return self.fact[value]



def main():
	n, m = map(int, sys.stdin.readline().split())
	fact = Fact(10**5)
	if abs(n - m) > 1:
		print(0)
		exit()
	ans = fact(n) * fact(m)
	if (n + m) % 2 == 0:
		ans *= 2
	print(ans)

main()
