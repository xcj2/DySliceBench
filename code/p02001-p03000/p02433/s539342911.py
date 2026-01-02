from sys import stdin

class QueueNode(object):
	def __init__(self,data,next=None,prev=None):
		self.data = data
		self.next = next
		self.prev = prev

class LinkList(object):
	def __init__(self,head=None):
		self.head = head
		self.tail = head
		self.cur  = head

	def insert_q(self,data):
		node = QueueNode(data)

		if self.cur is None:
			self.head = node
			self.tail = node
			self.cur  = node
			return

		currentNode = self.cur
		preNode = currentNode.prev

		if currentNode.prev is None:
			currentNode.prev = node
			node.next = currentNode
			self.head = self.cur = node
		else:
			if self.tail is not None:
				currentNode.prev = node
				node.prev = preNode
				node.next = currentNode
				preNode.next = node
				self.cur = node
			else:
				currentNode.next = node
				node.prev = currentNode
				node.next = None
				self.cur = node
				self.tail = node


	def move_q(self,mv):
		currentNode = self.cur
		cnt = mv
		while cnt != 0:
			if mv < 0:#prev
				if currentNode.prev is None:
					self.head = self.cur = currentNode
					break
				else:
					currentNode = currentNode.prev
					self.cur = currentNode
					cnt += 1
			else:#next
				if currentNode.next is None:
					self.cur = currentNode
					break
				else:
					currentNode = currentNode.next
					self.cur = currentNode
					cnt -= 1


	#カレントを削除する
	def delete_q(self):
		currentNode = self.cur
		nexNode = currentNode.next
		preNode = currentNode.prev

		#自身の前がいない（=先頭）
		if preNode is None:
			nexNode.prev = None
			self.head = nexNode
			self.cur = nexNode
		#自身の後ろがいない（=末尾）
		elif nexNode is None:
			preNode.next = None
			self.tail = None
		else:
			preNode.next = currentNode.next
			nexNode.prev = currentNode.prev
			self.cur = currentNode.next

	#先頭を表示する
	def print_q(self):
		if self.head is not None:
			print(self.head.data)

	#全体表示（先頭から）
	def print_all(self):
		if self.head is not None:
			currentNode = self.head
			while currentNode.next is not None:
				print(currentNode.data)
				currentNode = currentNode.next

if __name__ == '__main__':

	loopnum = int(input())

	ll = LinkList()
	ll.insert_q("E")
	for i in range(loopnum):
		cmd = stdin.readline().strip().split()
		if cmd[0] == "0":
			t = int(cmd[1])
			ll.insert_q(t)
		elif cmd[0] == "1":
			t = int(cmd[1])
			ll.move_q(t)
		else:
			ll.delete_q()
	ll.print_all() 

