
def read_input():
    s = input()
    t = input()

    return s, t


# 長さn、tを含むパターンを形成
def make_pattern(n, t):
    m = len(t)

    patterns = []
    for i in range(n - m + 1):
        patterns.append(['?'] * i + t + ['?'] * (n - i - m))

    return patterns

# aとbの要素ごとの比較
# ?と*はいずれともマッチする
def check_match(a, b):
    def convert(x, y):
        if x == '?' and y == '?':
            return 'a'
        if x == y:
            return x
        if x == '?':
            return y
        if y == '?':
            return x
        return None

    result = []
    for i in range(len(a)):
        result.append(convert(a[i], b[i]))

    return result

def submit():
    s, t = read_input()

    s = [c for c in s]
    t = [c for c in t]

    patterns = make_pattern(len(s), t)

    candidates = [check_match(s, p) for p in patterns]
    candidates = [''.join(c) for c in candidates if None not in c]
    candidates.sort()

    if candidates:
        print(candidates[0])
    else:
        print('UNRESTORABLE')

if __name__ == '__main__':
    submit()