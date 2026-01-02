# for #!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
from math import gcd

def main():
		n = int(input())
		s = input()
		ans = 0
		b = [0]*n
		g = [0]*n
		r = [0]*n
		for i in range(n):
			if s[i]=="B":
				b[i]=1
			if s[i]=="G":
				g[i]=1
			if s[i]=="R":
				r[i]=1
		pre_r = [r[0]]
		pre_b = [b[0]]
		pre_g = [g[0]]
		for i in range(1,n):
			pre_r.append(pre_r[i-1]+r[i])
			pre_g.append(pre_g[i-1]+g[i])
			pre_b.append(pre_b[i-1]+b[i])	
		ms = {"R", "G", "B"}
		ans = 0
		for i in range(n):
			for j in range(i+1, n):
				if (s[i]!=s[j]):
					z = set([s[i], s[j]])
					x = list(ms.difference(z))[0]
					# print(i, j, ans)
					if x=="B":
						tmp = pre_b[j]-pre_b[i]
						if (i+j)/2 == int((i+j)/2):
							if b[(i+j)//2] == 1:
								tmp-=1
						ans += max(0, tmp)
					if x=="G":
						tmp = pre_g[j]-pre_g[i]
						# print((i+j)/2, "bahar")
						if (i+j)/2 == int((i+j)/2):
							# print("andar")
							# print()
							if g[(i+j)//2] == 1:
								tmp-=1
								# print("tmp", tmp)
						ans += max(0, tmp)					
					if x=="R":
						tmp = pre_r[j]-pre_r[i]
						if (i+j)/2 == int((i+j)/2):
							if r[(i+j)//2] == 1:
								tmp-=1
						ans += max(0, tmp)
		print(ans)
		
		


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