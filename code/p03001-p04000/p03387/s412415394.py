import heapq
class PriorityQueue:
	"""
	動的に優先度付きで値をpopする
	値を変更してから再度ソートして取り出すみたいな操作をするなら
	Priority Queue!
	"""
	def __init__(self,num_list=None,reverse=False):
		self.reverse = reverse
		self.heap = []
		if num_list != None :
			for num in num_list:
				self.push(num)

	def push(self,num):
		heapq.heappush(self.heap,-num if self.reverse else num)

	def pop(self):
		num = heapq.heappop(self.heap)
		return -num if self.reverse else num
	
	def get(self):
		return list(map(lambda x: x*(-1),self.heap))


def cmd1(a,b):
	return a+1,b+1

def cmd2(n):
	return n+2

a,b,c = map(int,input().split())
const = min(a,b,c)
a -= const
b -= const
c -= const
count = 0
pq = PriorityQueue(num_list=[a,b,c],reverse=True)
total = 0
while True :
	num_max = pq.pop()
	a = pq.pop()
	b = pq.pop()

	a_req = num_max - a
	b_req = num_max - b
	
	if num_max == a == b :
		break

	if a_req > 0 and b_req > 0:
		a,b = cmd1(a,b)
		total += 1
	else :
		b = cmd2(b)
		total += 1
	pq.push(num_max)
	pq.push(a)
	pq.push(b)
print(total)