import math

class Input():
	def readInt(self):
		return int(input())

	def readIntArray(self):
		return [int(x) for x in input().split(" ")]

	def readString(self):
		return input()

	def readStringArray(self):
		return input().split(" ")

	def readFloat(self):
		return float(input())

	def readFloatArray(self):
		return [float(x) for x in input().split(" ")]

def main():
	inp = Input()
	_ = inp.readInt()
	s1, s2 = inp.readStringArray()

	output = ""
	for c1, c2 in zip(s1, s2):
		output += (c1 + c2)

	print(output)


if __name__ == "__main__":
   main()
