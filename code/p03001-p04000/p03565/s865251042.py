# encoding:utf-8

def main():
	s = list(input())
	t = list(input())
	print(checker(s, t))

def checker(s, t):
	for i in range(len(s)):
		if i >= len(t) - 1:
			if checker2(s, t, len(s) - i - 1):
				for i2 in range(len(t)):
					s[len(s) - i  - 1 + i2] = t[i2]
				for i2 in range(len(s)):
					if s[i2] == "?":
						s[i2] = "a"
				return "".join(s)

	return "UNRESTORABLE"


def checker2(s, t, i):
	for i2 in range(len(t)):
		#print(i, i2)
		#print(s[i + i2], t[i2])
		if s[i + i2] == "?":
			continue
		elif s[i + i2] == t[i2]:
			continue
		else:
			return False

	return True



if __name__ == '__main__':
	main()