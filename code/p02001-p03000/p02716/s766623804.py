# for #!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
from collections import defaultdict

def main():
	# for t in range(int(input())):
	n = int(input())
	l = [int(j) for j in input().split()]
	dp = dict()
	dp[0,0] = 0
	dp[2,1] = max(l[0], l[1])
	dp[1,1] = l[0]
	dp[2,2] = -1e14
	dp[1, 0] = 0
	for i in range(3,n+1):
		for j in [(i//2), (i+1)//2]:
			# print(i, j)
			# if (i+j)%2==1:
			dp[i, j] = dp[i-2, j-1]+l[i-1]
			if i>=2*j:
				dp[i, j] = max(dp[i-2, j-1]+l[i-1], dp[i-1, j])				
				
			# else:
			# dp[i, j] = dp[i-2, j-1]+l[i-1]

			# if dp[i, j]
	print(dp[n, (n)//2])
		


# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
	newlines = 0

	def __init__(self, file):
		self._fd = file.fileno()
		self.buffer = BytesIO()
		self.writable = "x" in file.mode or "r" not in file.mode
		self.write = self.buffer.write if self.writable else None

	def read(self):
		while True:
			b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
			if not b:
				break
			ptr = self.buffer.tell()
			self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
		self.newlines = 0
		return self.buffer.read()

	def readline(self):
		while self.newlines == 0:
			b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
			self.newlines = b.count(b"\n") + (not b)
			ptr = self.buffer.tell()
			self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
		self.newlines -= 1
		return self.buffer.readline()

	def flush(self):
		if self.writable:
			os.write(self._fd, self.buffer.getvalue())
			self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
	def __init__(self, file):
		self.buffer = FastIO(file)
		self.flush = self.buffer.flush
		self.writable = self.buffer.writable
		self.write = lambda s: self.buffer.write(s.encode("ascii"))
		self.read = lambda: self.buffer.read().decode("ascii")
		self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
	main()