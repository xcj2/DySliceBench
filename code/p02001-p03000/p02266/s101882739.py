from typing import Generic, List, TypeVar

T = TypeVar('T')

class Stack(Generic[T]):
	def __init__(self) -> None:
		self._container: List[T] = []
					
	@property
	def empty(self) -> bool:
		return not self._container # コンテナが空ならば真となる
	
	def push(self, item: T) -> None:
		self._container.append(item)

	def pop(self) -> T:
		return self._container.pop() # LIFO
	
	def __repr__(self) -> str:
		return repr(self._container)


if __name__ == "__main__":
	stack1 = Stack()
	stack2 = Stack()
	string = input()
	sum = 0
	for i in range(len(string)):
		if string[i] == "\\":
			stack1.push(i)
		elif string[i] == "_":
			pass
		elif string[i] == "/":
			if not stack1.empty:
				j = stack1.pop()
				sum += i - j
				a = i - j
				while not stack2.empty:
					item = stack2.pop()
					if item[0] <= j:
						stack2.push(item)
						break
					else:
						a += item[1]
				stack2.push((j, a))
	print(sum)
	b = []
	while not stack2.empty:
		b.append(str(stack2.pop()[1]))
	b.append(str(len(b)))
	b.reverse()
	print(' '.join(b))

