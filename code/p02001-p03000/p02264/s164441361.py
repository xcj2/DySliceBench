from typing import TypeVar, Generic, List, Deque

T = TypeVar('T')

class Queue(Generic[T]):
	def __init__(self) -> None:
		self._container: Deque[T] = Deque()

	@property
	def empty(self) -> bool:
		return not self._container # コンテナが空ならば真となる

	def push(self, item: T):
		self._container.append(item)

	def pop(self) -> T:
		return self._container.popleft() # FIFO

	def __repr__(self) -> str:
		return repr(self._container)


if __name__ == "__main__":
	a = list(map(int, input().split()))
	n = a[0]
	q = a[1]
	queue = Queue()
	for _ in range(n):
		b = list(input().split())
		queue.push([b[0], int(b[1])])
	time = 0
	while not queue.empty:
		item = queue.pop()
		if item[1] - q <= 0:
			time += item[1]
			print(f"{item[0]} {time}")
		else:
			item[1] -= q
			queue.push(item)
			time += q
