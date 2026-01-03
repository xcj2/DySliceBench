import math
from operator import itemgetter

def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a
 
def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)
 

def f(b,n):
	if n < b:
		return n
	return f(b, n//b) + n%b
 
# 4 3
# 1 2 1420
# 2 3 1120
# 3 4 1420

N = int(input())
nums = [int(input()) for _ in range(N)]

all10 = True
for elem in nums:
	if elem % 10 != 0:
		all10 = False
		break

if(all10):
	print(0)
	exit()

min_nums = []
for i in range(0,len(nums)):
	if(nums[i] % 10 != 0 ):
		min_nums.append(nums[i])



if(sum(nums) % 10 == 0):
	print(sum(nums)-min(min_nums))
else:
	print(sum(nums))