M = 10 ** 9 + 7

# inverse
def calc_inverse(n, law):
	if n == 1:
		return 1
	
	pre_r = law
	pre_x = 0
	pre_y = 1
	cur_r = n
	cur_x = 1
	cur_y = 0
	
	while True:
		d = pre_r // cur_r
		r = pre_r % cur_r
		
		nxt_r = r
		nxt_x = pre_x - d * cur_x
		nxt_y = pre_y - d * cur_y
		
		if nxt_r == 1:
			ret = nxt_x
			while ret < 0:
				ret += law;
			return ret;
		elif nxt_r == 0:
			return None
		
		pre_r = cur_r;
		pre_x = cur_x;
		pre_y = cur_y;
		cur_r = nxt_r;
		cur_x = nxt_x;
		cur_y = nxt_y;

facts = [1]
facts_i = [1]
def cache_facts(n, M):
	f = 1
	fi = 1
	for i in range(1, n):
		f = (f * i) % M
		fi = (fi * calc_inverse(i, M)) % M
		facts.append(f)
		facts_i.append(fi)

def cached_C(a, b, M):
	return facts[a] * facts_i[a - b] * facts_i[b] % M

K = int(input())
S = input().strip()
L = len(S)

cache_facts(K + L + 1, M)

total = pow(26, K, M)

#print(total)
for i in range(1, K + 1):
	total = (total + (pow(25, i, M) * cached_C(L + i - 1, L - 1, M) % M) * pow(26, K - i, M)) % M

print(total)

