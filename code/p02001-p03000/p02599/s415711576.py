#dt = {} for i in x: dt[i] = dt.get(i,0)+1
import sys;input = sys.stdin.readline
inp,ip = lambda :int(input()),lambda :[int(w) for w in input().split()]
'''
from queue import PriorityQueue
n,k = ip()
x = ip()
pq = PriorityQueue()
for i in x:
    pq.put((-1)*i)
print(sorted(x,reverse=True))
for i in range(k):
    ele = abs(pq.get())
    print(ele)
    if ele%2:
        pq.put((-1)*(ele//2))
        pq.put((-1)*((ele//2) +1))
    else:
        pq.put((-1)*(ele//2))
        pq.put((-1)*(ele//2))
print(abs(pq.get()))
'''
#dt = {} for i in x: dt[i] = dt.get(i,0)+1
import sys;input = sys.stdin.readline
inp,ip = lambda :int(input()),lambda :[int(w) for w in input().split()]

# Python3 code to find number of 
# distinct numbers in a subarray 
MAX = MAX = 1000001

# structure to store queries 
class Query: 
	def __init__(self, l, r, idx): 
		self.l = l 
		self.r = r 
		self.idx = idx 

# updating the bit array 
def update(idx, val, bit, n): 
	while idx <= n: 
		bit[idx] += val 
		idx += idx & -idx 

# querying the bit array 
def query(idx, bit, n): 
	summ = 0
	while idx: 
		summ += bit[idx] 
		idx -= idx & -idx 
	return summ 

def answeringQueries(arr, n, queries, q): 

	# initialising bit array 
	bit = [0] * (n + 1) 

	# holds the rightmost index of 
	# any number as numbers of a[i] 
	# are less than or equal to 10^6 
	last_visit = [-1] * MAX

	# answer for each query 
	ans = [0] * q 

	query_counter = 0
	for i in range(n): 

		# If last visit is not -1 update -1 at the 
		# idx equal to last_visit[arr[i]] 
		if last_visit[arr[i]] != -1: 
			update(last_visit[arr[i]] + 1, -1, bit, n) 

		# Setting last_visit[arr[i]] as i and 
		# updating the bit array accordingly 
		last_visit[arr[i]] = i 
		update(i + 1, 1, bit, n) 

		# If i is equal to r of any query store answer 
		# for that query in ans[] 
		while query_counter < q and queries[query_counter].r == i: 
			ans[queries[query_counter].idx] = query(queries[query_counter].r + 1, bit, n) - query(queries[query_counter].l, bit, n) 
			query_counter += 1

	# print answer for each query 
	for i in range(q): 
		print(ans[i]) 

# Driver Code 
if __name__ == "__main__": 
    n,q = ip()
    a = ip()
    queries = []
    for i in range(q):
        l,r = ip()
        queries.append(Query(l-1,r-1,i))
    queries.sort(key = lambda x: x.r) 
    answeringQueries(a, n, queries, q) 



