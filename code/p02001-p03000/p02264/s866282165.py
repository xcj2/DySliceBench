
class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class SimpleQeueue:
	def __init__(self):
		self.size = 0
		self.head = None
		self.tail = None
		return

	def enqueue(self, value):
		node = Node(value)
		if self.head == None:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node
		self.size += 1

	def dequeue(self):
		if self.is_empty() == True:
			return None
		node = self.head
		self.head = self.head.next
		self.size -= 1
		if self.is_empty() == True:
			self.head = None
			self.tail = None
		return node.value

	def peek(self):
		if self.is_empty() == True:
			return None
		return self.head.value

	def get_size(self):
		return self.size

	def is_empty(self):
		return self.size == 0

	def __str__(self):
		str_ = '['
		current = self.head
		while current != None:
			str_ += str(current.value)
			current = current.next
			if current != None:
				str_ += ', '
		str_ += ']['
		if self.tail != None:
			str_ += str(self.tail.value)
		str_ += ']'
		return str_

class Process:
	def __init__(self, name, time):
		self.name = name
		self.time = int(time)

	def set_time(self, time):
		self.time = time

n, q = map(int, input().split())
myqueue = SimpleQeueue()
for i in range(n):
	name, time = map(str, input().split())
	myqueue.enqueue(Process(name, time))

time_elapsed = 0
while myqueue.is_empty() != True:
	process = myqueue.dequeue()
	time = process.time
	if time > q:
		process.set_time(time - q)
		time_elapsed += q
		myqueue.enqueue(process)
	else:
		time_elapsed += time
		print(process.name + ' ' + str(time_elapsed))

