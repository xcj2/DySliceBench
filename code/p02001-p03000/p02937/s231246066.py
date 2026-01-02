import bisect

s = input()
t = input()
s_length = len(s)
t_length = len(t)

def char2int(char):
    return ord(char) - 97

def search_index(t_atom, last_index, d_list):
    t_atom_int = char2int(t_atom)
    d = d_list[t_atom_int]

    if d == []:
        return -1

    c = bisect.bisect_right(d, last_index)

    if c != len(d):
        return d[c]
    else:
        return d[0]

def solve():
    last_index = -1
    t_index = []
    loop_cost = 1

    d = [[] for _ in range(26)]
    for i in range(s_length):
        char = s[i]
        d[char2int(char)].append(i)

    for i in range(t_length):
        t_atom = t[i]
        t_atom_index = search_index(t_atom, last_index, d)
        if t_atom_index == -1:
            return -1
        else:
            t_index.append(t_atom_index)
            last_index = t_atom_index

    remainder_cost = t_index[-1] + 1

    for i in range(1, t_length):
        if t_index[i - 1] >= t_index[i]:
            loop_cost += 1

    return s_length * (loop_cost - 1) + remainder_cost

print(solve())
