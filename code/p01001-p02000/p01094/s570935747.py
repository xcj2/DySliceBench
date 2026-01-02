import sys
from collections import Counter, defaultdict
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def LIST(): return list(map(int, input().split()))

ans = []
while 1:
	n = INT()
	if n == 0:
		break
	c = input().split()

	cnt = Counter(c)
	tmp = cnt.most_common()
	if len(tmp) == 1:
		ans.append("{} {}".format(tmp[0][0], n//2+1))
	elif tmp[0][1] == tmp[1][1]:  # 引き分け
		ans.append("TIE")
	else:  # 決着がつく
		count = defaultdict(int)
		count["hoge"] += 1
		for i in range(n):
			count[c[i]] += 1
			max_ = max(count.values())
			if max_ > n//2:  # 決定
				ans.append("{} {}".format(tmp[0][0], i+1))
				break
			for j in count:  # すべてのキーのとりうる最大得点を求める．
				# print(j, count[j] + (n-i-1))
				if j != tmp[0][0] and count[j] + (n-i-1) >= max_:
					break
			else:  # もうこえない
				ans.append("{} {}".format(tmp[0][0], i+1))
				break
			
for x in ans:
	print(x)

