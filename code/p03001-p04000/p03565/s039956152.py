# enumerate の 番号が降順 のもの. 最後が0になる
def reverse_enumerate(l):
	for i, l_i in zip(range(len(l)-1, -1, -1), l):
		yield i, l_i
# n-gram(調べて)
def n_gram(s, n):
	return [s[i:i+n] for i in range(len(s)-n+1)]
# 二つの文字列が等しいかを調べる. 全ての文字と等しくなる文字を設定可能(all_match)
def is_equal_match(s1, s2, all_match=[]):
	for i in range(len(s1)):
		if not (s1[i] == s2[i] or s1[i] in all_match):
			return False
	return True
# 指定した index に 文字列を埋め込む
def fill_in_str(text, s, n):
	return text[:n] + s + text[n+len(s):]

s_ = input()
t = input()

for i, s_i in reverse_enumerate(n_gram(s_, len(t))[::-1]):
	if is_equal_match(s_i, t, all_match="?"):
		print(fill_in_str(s_, t, i).replace("?", "a"))
		exit()
print("UNRESTORABLE")