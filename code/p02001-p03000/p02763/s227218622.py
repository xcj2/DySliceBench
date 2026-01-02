class SegmentTree:
	def __init__(self, n, *, init = None, data = None, merge = None):
		if init != None and data != None:
			raise Error("init and data cannot be specified at a time")
		if init == None and data == None:
			raise Error("one of init or data must be specified")
		self.n = n
		data_table = []
		if data:
			data_table.append((1, data))
		else:
			data_table.append((1, tuple(init(i, i + 1) for i in range(n))))
		
		w = 2
		if merge == None:
			while w <= n:
				data_table.append((w, tuple(init(i, i + w) for i in range(0, ((n - 1) // w + 1) * w, w))))
				w *= 2
		else:
			last_data = data_table[0][1]
			while w <= n:
				if len(last_data) % 2 == 0:
					new_data = tuple(merge(last_data[i * 2], last_data[i * 2 + 1]) for i in range(0, (n - 1) // w + 1))
				else:
					new_data = tuple(merge(last_data[i * 2], last_data[i * 2 + 1]) for i in range(0, (n - 1) // w)) + (merge(last_data[-1], None), )
				data_table.append((w, new_data))
				last_data = new_data
				w *= 2
		self.data_table = data_table
		
	def data_at(self, i):
		for w, data_list in self.data_table:
			yield data_list[i // w]
	
	def data_range(self, s, e = None):
		if e == None:
			e = s
			s = 0
		if s == 0:
			for w, data_list in reversed(self.data_table):
				if e % (w * 2) >= w:
					yield data_list[e // w - 1]
		elif s < e:
			for w, data_list in self.data_table:
				w2 = w * 2
				m = s % w2
				new_s = s + w2 - m
				if new_s > e:
					break
				if m != 0:
					yield data_list[s // w]
					s = new_s
			if s == e:
				return
			for w, data_list in reversed(self.data_table):
				new_s = s + w
				if new_s <= e:
					yield data_list[s // w]
					s = new_s
			
			return
			for w, data_list in self.data_table:
#				print(f"({s} - {e})")
				w2 = w * 2
				m = s % w2
				if m != 0:
					yield data_list[s // w]
					s += w2 - m
					if s == e:
						break
				m = e % w2
				if m != 0:
					yield data_list[e // w - 1]
					e -= m
					if s == e:
						break
	
	def check(self, merge):
		last_data = self.data_table[0][1]
		for w, data in self.data_table[1:]:
			if len(last_data) % 2 == 0:
				new_data = tuple(merge(last_data[i * 2], last_data[i * 2 + 1]) for i in range(0, (self.n - 1) // w + 1))
			else:
				new_data = tuple(merge(last_data[i * 2], last_data[i * 2 + 1]) for i in range(0, (self.n - 1) // w)) + (last_data[-1], )
			if new_data != data:
				print(new_data)
				print(data)
				raise "hoge"
			last_data = new_data
			w *= 2
	
	def output(self, func):
		for w, data_list in self.data_table:
#			print(f"#{w}: " + ", ".join(func(data) for data in data_list))
			pass


A = ord("a")
N = int(input())
S = list(map(lambda c: ord(c) - A, input().strip()))
Q = int(input())

def count(s, e):
	counts = [0] * 26
	for i in range(s, min(N, e)):
		counts[S[i]] += 1
	return counts

def merge(count1, count2):
	result = list(count1)
	if count2 != None:
		for i in range(26):
			result[i] += count2[i]
	return result

st = SegmentTree(N, init = count, merge = merge)
#st.check(merge)

def set2str(s):
	return "".join(chr(A + j) if s[j] > 0 else "" for j in range(26))

for _ in range(Q):
	t, i, q = input().split()
	
	if t == "1":
		i = int(i) - 1
		q = ord(q) - A
		s = S[i]
		for data in st.data_at(i):
			data[s] -= 1
			data[q] += 1
		S[i] = q
		
#		st.check(merge)
		
	else:
		l = int(i) - 1
		r = int(q)
		result = [0] * 26
		for data in st.data_range(l, r):
			for i in range(26):
				result[i] += data[i]
		
		count = 0
		for i in range(26):
			if result[i] > 0:
				count += 1
#		st.output(lambda data: "".join(chr(A + j) + str(data[j]) if data[j] > 0 else "" for j in range(26)))
		
		print(count)
#		print("".join(set2str(data) for data in st.data_table[0][1]))

