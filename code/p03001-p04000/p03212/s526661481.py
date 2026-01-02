import math
def is_753(s) :
	
	if ("0" in s) :
		return False
	elif ("1" in s) :
		return False
	elif ("2" in s) :
		return False
	elif ("4" in s) :
		return False
	elif ("6" in s) :
		return False
	elif ("8" in s) :
		return False
	elif ("9" in s) :
		return False
	
	if ("7" in s and "5" in s and "3" in s) :
		return True
	
	return False

def hoge(s) :
	for i in range(len(s)) :
		if (s[i] != "3" and s[i] != "5" and s[i] != "7") :
			return int(math.pow(10, len(s) - (i+1)))

	return 0

def main() :
	N = int(input())
	count = 0
	index = 356
	
	if (N < 357) :
		print("0")
		return

	while index <= N :
		s = str(index)
		a = hoge(s)
		if (a != 0) :
			index += a
			continue		
		
		if (is_753(s)) :
			count += 1
		
		index += 1
	
	print(count)


main()