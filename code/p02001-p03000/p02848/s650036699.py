import os


def alpha2num(alpha):
    num=0
    for index, item in enumerate(list(alpha)):
        num += pow(26,len(alpha)-index-1)*(ord(item)-ord('A')+1)
    return num

def num2alpha(num):
    if num<=26:
        return chr(64+num)
    elif num%26==0:
        return num2alpha(num//26-1)+chr(90)
    else:
        return num2alpha(num//26)+chr(64+num%26)

def main():
	n = int(input())
	s = input()
	result = ""
	for i in s:
		num = alpha2num(i)
		if num + n > 26:
			num = num + n - 26
		else:
			num += n
		string = num2alpha(num)
		result += string
	print(result)
	

if __name__ == "__main__":
	main()
