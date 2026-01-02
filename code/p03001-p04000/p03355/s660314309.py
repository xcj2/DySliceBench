def f(s, t):
    n = len(t)
    r = set()
    i = 0
    while True:
        i = s.find(t, i)
        if i == -1:
            break
        cand = s[i: (i+n)+1]
        if len(cand) == n + 1:
            r.add(cand)
        i += 1
    return sorted(r)

class Counter:
    def __init__(self, K):
        self._cnt = 0
        self.cur_c = ''
        self.K = K

    @property
    def cnt(self):
        return self._cnt

    @cnt.setter
    def cnt(self, i):
        self._cnt = i
        if self._cnt == K:
            raise ValueError

if __name__ == '__main__':
    s = input()
    K = int(input())

    l = sorted(set(s))



    ctr = Counter(K)
    try:
        for c1 in l:
            ctr.cur_c = c1
            ctr.cnt += 1
            for c2 in f(s, c1):
                ctr.cur_c = c2
                ctr.cnt += 1
                for c3 in f(s, c2):
                    ctr.cur_c = c3
                    ctr.cnt += 1
                    for c4 in f(s, c3):
                        ctr.cur_c = c4
                        ctr.cnt += 1
                        for c5 in f(s, c4):
                            ctr.cur_c = c5
                            ctr.cnt += 1
    except ValueError:
        print(ctr.cur_c)
