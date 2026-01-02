from collections import Counter

mod = pow(10, 9)+7
n, k = map(int, input().split())
arr = list(map(int, input().split()))

BIT = [0]*(n+1)

def map_arr():
	dct = {}
	idx = 1
	lst = sorted(arr)
	for i in range(n):
		if lst[i] not in dct:
			dct[lst[i]] = idx 
			idx += 1
	return [dct[ele] for ele in arr]

arr = map_arr()
def get_add():
	counter = Counter(arr)
	lst = sorted(counter.items())
	add = lst[0][1]
	dp = [0]*len(lst)
	for i in range(1, len(lst)):
		dp[i] = lst[i-1][1] + dp[i - 1]
	return sum(dp[i]*lst[i][1] for i in range(len(lst)))

def read(idx):
	add = 0
	while idx > 0:
		add += BIT[idx]
		idx -= (-idx & idx)
	return add 

def update(idx):
	while idx <= n:
		BIT[idx] += 1
		idx += (-idx & idx)

inv_count = 0

for i in range(n-1, -1, -1):
	inv_count += read(arr[i]-1)
	update(arr[i])
ans = (k*inv_count)%mod

add = get_add()
multi = (k*(k-1)//2)%mod
ans = (ans + (multi*add)%mod)%mod
print(ans)