n_str = input()
k = int(input())

def k1(n_str):
	n_str = str(int(n_str))
	n_len = len(n_str)
	return 9*(n_len-1) + int(n_str[0])

def k2(n_str):
    s = 0
    n_str = str(int(n_str))
    n_len = len(n_str)
    if n_len < 2:
        return 0
    s += k2('9'*(n_len - 1))
    s += k1('9'*(n_len - 1)) * (int(n_str[0]) - 1)
    s += k1(n_str[1:])
    return s
                      
def k3(n_str):
    s = 0
    n_str = str(int(n_str))
    n_len = len(n_str)
    if n_len < 3:
        return 0
    s += k3('9'*(n_len - 1))
    s += k2('9'*(n_len - 1)) * (int(n_str[0]) - 1)
    s += k2(n_str[1:])
    return s

if k == 1:
    print(k1(n_str))
elif k == 2:
    print(k2(n_str))
elif k == 3:
    print(k3(n_str))