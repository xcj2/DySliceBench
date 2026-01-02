class ZAlgorithm(object):
    def __init__(self, s: str):
        self.orig_str = s
        self.Z = self.__create_z(s)

    def __call__(self, i: int):
        return self.Z[i]

    def __create_z(self, s: str):
        n = len(s)
        Z = [0]*n
        Z[0] = n
        l, r = 0, 0

        for t in range(1, n):
            if t>r:
                z = 0
                while t+z<n and s[0+z]==s[t+z]:
                    z += 1
                Z[t] = z
                if z>0:
                    l, r = t, t+z-1
            else:
                p, b = t-l, r-t+1
                if Z[p]<b:
                    Z[t] = Z[p]
                else:
                    i = r+1
                    while i<n and s[i]==s[i-t]:
                        i += 1
                    Z[t] = i-t
                    l, r = t, i-1
        return Z

def f_e():
    n = int(input())
    s = input()
    a = 0
    for i in range(n-1):
        ss = s[i:]
        z_algo = ZAlgorithm(ss)
        for j in range(len(ss)):
            a = max(a, min(z_algo(j), j))
    print(a)

if __name__ == "__main__":
    f_e()
