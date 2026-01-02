import sys

def input():
    return sys.stdin.readline()[:-1]

N = int(input())

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

def func1(lst, value):
    return [i for i, x in enumerate(lst) if x <= value]

if N == 1:
	print(0)
else:
	
	ans_ = factorization(N)
	nums = []
	index_list = []
	
	ans = 0
	for i in range(1, 100):
		ans += i
		index_list.append(ans)
		
	for a in ans_:
		#nums.append(int(format(a[1], 'b')))
		nums.append(a[1])
		
		#print(nums)
			
	ans = 0
	for i in nums:
		index = func1(index_list, i)
		#print(max(index)+1)
		ans += max(index)+1
	
	print(ans)
