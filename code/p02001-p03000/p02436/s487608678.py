from sys import stdin

class QueueNode(object):
	def __init__(self,data,next=None):
		self.data = data
		self.next = next

class LinkList(object):
	def __init__(self,head=None):
		self.head = head
		self.tail = head

	#後ろに挿入する
	def insert_q(self,data):
		node = QueueNode(data)

		if self.head is None:
			self.head = node
			self.tail = node
			return

		currentNode = self.tail

		while True:
			if currentNode.next is None:
				currentNode.next = node
				self.tail = node
				break
			currentNode = currentNode.next

	#先頭を削除する
	def delete_q(self):
		if self.head is not None:
			currentNode = self.head
			self.head = currentNode.next

	#先頭を表示する
	def print_q(self):
		if self.head is not None:
			print(self.head.data)

if __name__ == '__main__':

	qnum,loopnum = map(int,input().split(" "))

	q = [LinkList() for i in range(qnum)]

	for i in range(loopnum):
		cmd = stdin.readline().strip().split()
		t = int(cmd[1])
		if cmd[0] == "0":
			q[t].insert_q(int(cmd[2]))
		elif cmd[0] == "1":
			q[t].print_q()
		else:
			q[t].delete_q()



