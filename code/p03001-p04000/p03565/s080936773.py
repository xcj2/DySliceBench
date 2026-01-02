import copy

def check(s, t, k):
	for i in range(len(t)):
		if s[i+k] != t[i] and s[i+k] != '?':
			return False
	return True

def construct(s, t, k):
	ans = copy.deepcopy(s)
	for i in range(len(t)):
		ans[i+k] = t[i]
	for i in range(len(s)):
		if ans[i] == '?':
			ans[i] = 'a'
	return "".join(ans)

def resolve():
	s = list(input())
	t = list(input())
	ans = []
	if len(s) < len(t):
		print('UNRESTORABLE')
		return
	for i in range(len(s) - len(t) + 1):
		if check(s, t, i):
			ans.append(construct(s, t, i))
	if len(ans) >= 1:
		print(min(ans))
	else:
		print('UNRESTORABLE')
resolve()