# -*- coding: utf-8 -*-
import sys

def main():
	Sa = list(input())
	Sb = list(input())
	Sc = list(input())

	next = "a"
	qa = Queue()
	qb = Queue()
	qc = Queue()
	for i in Sa:
		qa.enqueue(i)
	for i in Sb:
		qb.enqueue(i)
	for i in Sc:
		qc.enqueue(i)

	while True:
		if next == "a":
			next = qa.dequeue()
			if next == None:
				print("A");
				sys.exit();
		if next == "b":
			next = qb.dequeue()
			if next == None:
				print("B");
				sys.exit();
		if next == "c":
			next = qc.dequeue()
			if next == None:
				print("C");
				sys.exit();

class Queue:
    def __init__(self, queue = None):
        if type(queue) is type([]):
            self.queue = queue
        else:
            self.queue = []

    def enqueue(self, e):
        self.queue.append(e)
        return self.queue

    def dequeue(self):
        try:
            qEl = self.queue[0]
            del self.queue[0]
            return qEl
        except IndexError:
            return None


if __name__ == "__main__":
	main()
