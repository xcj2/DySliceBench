s = input()
t = input()

alphabet = [chr(i) for i in range(97, 97+26)]


def max_s(s):
    for c in alphabet:
        if c in s:
            return c


def min_s(s):
    for c in reversed(alphabet):
        if c in s:
            return c


def compare(s1, s2):
    s1_index = alphabet.index(s1)
    s2_index = alphabet.index(s2)
    return s1_index < s2_index


for i in range(max(len(s), len(t))):
    if len(s) == 0:
        print("Yes")
        break
    elif len(t) == 0:
        print("No")
        break

    s_max = max_s(s)
    t_min = min_s(t)

    if s_max == t_min:
        s = s[:s.find(s_max)] + s[s.find(s_max) + 1:]
        t = t[:t.find(t_min)] + t[t.find(t_min) + 1:]
        continue

    if compare(s_max, t_min):
        print("Yes")
        break
    else:
        print("No")
        break
else:
    print("No")
