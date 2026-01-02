class ZAlgorithm(object):
    def __init__(self, s: str):
        self.lcp = self.__create_z(s)

    def __call__(self, i: int):
        return self.lcp[i]

    def __create_z(self, s: str):
        n = len(s)
        lcp = [n] + [0]*(n-1)
        l, r = 0, 0

        for t in range(1, n):
            if t>r:
                z = 0
                while t+z<n and s[0+z]==s[t+z]:
                    z += 1
                lcp[t] = z
                if z>0:
                    l, r = t, t+z-1
            else:
                p, b = t-l, r-t+1
                if lcp[p]<b:
                    lcp[t] = lcp[p]
                else:
                    i = r+1
                    while i<n and s[i]==s[i-t]:
                        i += 1
                    lcp[t] = i-t
                    l, r = t, i-1
        return lcp

def main():
    n, s = open(0).read().split()
    a = 0
    for i in range(int(n)-1):
        ss = s[i:]
        z_algo = ZAlgorithm(ss)
        for j in range(len(ss)):
            a = max(a, min(z_algo(j), j))
    print(a)

if __name__ == "__main__":
    main()
