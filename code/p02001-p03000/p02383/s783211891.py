# coding: utf-8
# ?????????????????¨????????????
class Dice(object):
	def __init__(self):
		# ???????????????????????°
		# ????????¶???
		self.x = [2, 5]
		self.y = [3, 4]
		self.z = [1, 6]
		SN = {'S': 0, 'N': 1}
		WE = {'W': 0, 'E': 1}
		pass

	def rotate(self, _dir):
		def rot(_k, _r):
			return list(reversed(_r)), _k

		if _dir=='N':
			self.x, self.z = rot(self.x, self.z)
		elif _dir=='S':
			self.z, self.x = rot(self.z, self.x)
		elif _dir=='E':
			self.z, self.y = rot(self.z, self.y)
		elif _dir=='W':
			self.y, self.z = rot(self.y, self.z)
		else:
			pass

	def top(self):
		return self.z[0]


if __name__=="__main__":
	dice = Dice()
	val = list(map(int, input().split()))
	dr = input()
	for d in dr:
		dice.rotate(d)
	print(val[dice.top()-1])