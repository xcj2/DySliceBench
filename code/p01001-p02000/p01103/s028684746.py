import sys
from itertools import permutations, combinations, product

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def LIST(): return list(map(int, input().split()))
def MAP(): return map(int, input().split())

ans = []
while 1:
	d, w = MAP()
	if d == 0 and w == 0:
		break
	e = [LIST() for _ in range(d)]
	sum_max = 0
	for i in combinations(range(d), 2):
		if abs(i[0]-i[1]) == 1:
			continue
		for j in combinations(range(w), 2):
			if abs(j[0]-j[1]) == 1:
				continue
			# 堀の最小値を見つける
			min_ = 10
			for k in range(i[0], i[1]+1):
				if k == i[0] or k == i[1]:
					for l in range(j[0], j[1]+1):
						min_ = min(min_, e[k][l])
				else:
					min_ = min(min_, e[k][j[0]])
					min_ = min(min_, e[k][j[1]])
			# 内側を調べる．内側にmin_以上の値があればだめ．
			sum_ = 0
			for k in range(i[0]+1, i[1]):
				for l in range(j[0]+1, j[1]):
					# print(k, l, e[k][l])
					if e[k][l] >= min_:
						sum_ = 0
						break
					else:
						sum_ += (min_-e[k][l])
				if e[k][l] >= min_:
					break
			sum_max = max(sum_max, sum_)

	ans.append(sum_max)
for x in ans:
	print(x)

