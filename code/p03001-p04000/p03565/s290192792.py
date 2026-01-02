#  --*-coding:utf-8-*--

def f(S, T):
    lastIndex = None
    pat = None

    for i in range(len(S)-len(T)+1):
        pat2 = g(S, T, i)

        if pat2 != None and (pat == None or pat2 < pat):
            pat = pat2

    if pat == None:
        return 'UNRESTORABLE'

    S2 = list(S)
    for index, letter in pat:
        S2[-index] = letter

    return ''.join(S2).replace('?', 'a')
            


def g(S, T, st):
    pat = []

    for i in range(len(T)):
        s = S[st + i]
        t = T[i]

        if s == '?':
            if t != 'a':
                pat.append((-(st + i), t))
        elif s != t:
            return None

    return pat
        

def test():
    assert f('?tc????', 'coder') == 'atcoder'
    assert f('??p??d??', 'abc') == 'UNRESTORABLE'


def main():
    S = input()
    T = input()
    print(f(S, T))


if __name__ == '__main__':
    main()
