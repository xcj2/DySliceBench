class Prime():
    def __init__(self, n):
        self.p = [] # self.p[i] = i番目の素数 < n
        self.d = [0] * n # self.d[i] = iを割り切る最小の素数

        # エラトステネスの篩
        for i in range(2, n):
            if self.d[i] == 0:
                self.p.append(i)
                for j in range(i, n, i):
                    if self.d[j] == 0:
                        self.d[j] = i

        self.ind = [-1] * n # self.ind[i] = self.p.index[i]
        for i in range(len(self.p)):
            self.ind[self.p[i]] = i

    def prime_factorization_index(self, x): # xの素因数のlistをreturn(重複なし)
        l = [self.ind[self.d[x]]]
        x //= self.d[x]
        while x != 1:
            if l[-1] != self.ind[self.d[x]]:
                l.append(self.ind[self.d[x]])
            x //= self.d[x]
        return l

    def num_prime(self): # n未満の素数の個数をreturn
        return len(self.p)

def main():

    from math import gcd
 
    n = int(input())
    a = list(map(int, input().split()))

    # 'not coprime'かどうか判定
    g = a[0]
    for i in a:
        g = gcd(g, i)
        if g == 1:
            break
    else:
        print('not coprime')
        exit()

    # 'setwise coprime'かどうか判定
    p = Prime(10**6 + 1)

    tf = [False] * p.num_prime() # tf[i] == True: i番目の素数を素因数とするものが存在する

    for i in a:
        if i == 1:
            continue

        l = p.prime_factorization_index(i)
        for j in l:
            if tf[j]:
                print('setwise coprime')
                exit()
            else:
                tf[j] = True

    print('pairwise coprime')

main()
