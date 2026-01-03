s = input()

def bit():
    if len(s) == 1:
        print(s)
    else:
        total = 0
        for i in range((2 ** (len(s) - 1))):
            bit = format(i, '0{}b'.format(len(s) - 1))
            e = ''
            for j in range(len(s) - 1):
                e += s[j]
                if bit[j] == '1':
                    e += '+'
            e += s[-1]
            total += eval(e)
        print(total)

def recursive():
    def _recurs(s):
        if len(s) == 1:
            return [s]
        with_plus = []
        without_plus = []
        for i in _recurs(s[1:]):
            with_plus.append('{}+{}'.format(s[0], i))
            without_plus.append('{}{}'.format(s[0], i))
        return with_plus + without_plus
    ans = _recurs(s)
    print(sum(eval(a) for a in ans))

answer = recursive
answer()
