import math

def str2list(str):
	result = []
	for value in str.split(' '):
		result.append(int(value))
	return result

def distance1(n, x, y):
	result = 0
	for i in range(n):
		result += abs(x[i] - y[i])
		
	return result
	
def distance2(n, x, y):
	result = 0
	for i in range(n):
		result += (x[i] - y[i]) * (x[i] - y[i])
		
	return math.sqrt(result) if result != 0 else 0
	
def distance3(n, x, y):
	result = 0
	for i in range(n):
		result += math.pow(abs(x[i] - y[i]), 3)
		
	return math.exp(math.log(result)/3) if result != 0 else 0
	
def distanceInf(n, x, y):
	result = 0
	for i in range(n):
		new_result = abs(x[i] - y[i])
		result = new_result if new_result > result else result
		
	return result

n = int(input());
x = str2list(input())
y = str2list(input())

print('%.6f'%distance1(n, x, y))
print('%.6f'%distance2(n, x, y))
print('%.6f'%distance3(n, x, y))
print('%.6f'%distanceInf(n, x, y))