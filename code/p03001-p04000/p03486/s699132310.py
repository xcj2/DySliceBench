
def read_input():
    s = input()
    t = input()
    return s, t


# s<tをチェックする
def greater_check(s, t):
    if len(s) < len(t):
        if s == t[:len(s)]:
            return True

    for i in range(min(len(s), len(t))):
        if s[i] < t[i]:
            return True

    return False

def submit():
    s, t = read_input()

    sc = [c for c in s]
    tc = [c for c in t]

    sc.sort()
    tc.sort(reverse=True)

    if greater_check(''.join(sc), ''.join(tc)):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    submit()