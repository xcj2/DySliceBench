from itertools import groupby

class Osa_k:
    def __init__(self, n_max):
        self.min_factor = min_factor = list(range(n_max+1))
        for i in range(2, int(n_max**0.5)+1):
            if min_factor[i] == i:
                for j in range(i*i, n_max+1, i):
                    if min_factor[j] == j:
                        min_factor[j] = i

    def __call__(self, n):
        min_factor = self.min_factor
        n_twoes = (n & -n).bit_length() - 1  # 最悪ケースでは速くなる
        res = [2] * n_twoes
        n >>= n_twoes
        while n > 1:
            p = min_factor[n]
            res.append(p)
            n //= p
        return res

def main():
    N = int(input())
    A = list(map(int, input().split()))
    osa_k = Osa_k(1010101)
    Factors = [osa_k(a) for a in A]
    factors = Factors[0]
    st0 = set(factors)  # 0 になれば setwize
    st1 = set(factors)  # 重複しなければ pairwise
    pairwise = True
    for factors in Factors[1:]:
        st = []
        for f, _ in groupby(factors):
            if f in st1:
                pairwise = False
            else:
                st1.add(f)
            st.append(f)
        st0 &= set(st)
    if pairwise:
        print("pairwise coprime")
    elif not st0:
        print("setwise coprime")
    else:
        print("not coprime")

main()
