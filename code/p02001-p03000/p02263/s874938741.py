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
	stack = Stack()
	a = list(input().split())
	for s in a:		
		if s == '+':
			x = stack.pop()
			y = stack.pop()
			stack.push(x + y)
		elif s == '-':
			x = stack.pop()
			y = stack.pop()
			stack.push(y - x)
		elif s == '*':
			x = stack.pop()
			y = stack.pop()
			stack.push(x * y)
		else:
			stack.push(int(s))
	print(stack.pop())
