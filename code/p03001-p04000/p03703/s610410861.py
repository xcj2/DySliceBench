import sys
input = sys.stdin.buffer.readline
import bisect

def main():
	N,K = map(int,input().split())
	cum = [0]
	for _ in range(N):
		cum.append(cum[-1]+int(input())-K)

	s_cum = sorted(cum)

	def invNumCount(A):
		l = len(A)
		res = 0
		BIT = [0]*(l+1)

		def BIT_query(idx):
			res_sum = 0
			while idx > 0:
				res_sum += BIT[idx]
				idx -= idx&(-idx)
			return res_sum

		def BIT_update(idx,x):
			while idx <= l:
				BIT[idx] += x
				idx += idx&(-idx)
			return

		Ai = [None]*l
		for i,e in enumerate(A):
			Ai[e] = i
		for i,e in enumerate(Ai):
			res += i - BIT_query(e+1)
			BIT_update(e+1,1)
		return res

	d = {}
	pos = [None]*(N+1)
	for i,num in enumerate(cum):
		ind = bisect.bisect_left(s_cum,num)
		if num not in d:
			d[num] = 1
		else:
			ind += d[num]
			d[num] += 1
		pos[i] = N-ind

	print(invNumCount(pos))

if __name__ == "__main__":
	main()