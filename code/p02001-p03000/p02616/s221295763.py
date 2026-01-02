#!/usr/bin/env python3

import sys


def main():
    mod = 1000000007                # 10^9+7
    def input():  return sys.stdin.readline().rstrip()
    def mi():     return map(int, input().split())
    def lmi():    return list(map(int, input().split()))
    def debug(x): print(x, file=sys.stderr)


    def check_positive(k, pos, neg):
        if k % 2 == 0:
            return (len(neg) // 2) * 2 + len(pos) >= k
        else:
            if pos:
                k -= len(pos) if len(pos) % 2 == 1 else len(pos) - 1
                return (len(neg) // 2) * 2 >= k
            return False

    def solve(n, k, L):
        pos = []
        zero_cnt = 0
        neg = []
        for elm in L:
            if elm < 0:
                neg.append(elm)
            elif elm > 0:
                pos.append(elm)
            else:
                zero_cnt += 1
        
        if check_positive(k, pos, neg):
            # 答えは正にできる。できるだけ大きい正の値を作ろう
            abs_neg = []
            tmp = sorted([abs(elm) for elm in neg], reverse=True)
            i = 0
            while i + 1 < len(tmp):
                abs_neg.append(tmp[i] * tmp[i+1])
                i += 2
            abs_neg.reverse()
            neg = abs_neg    # 昇順
            pos.sort()    # 昇順
            mul = 1
            cnt = 0
            # print(pos)
            # print(neg)
            while cnt < k:
                if pos and neg:
                    if (k - cnt) % 2 == 1:
                        mul = (mul * pos.pop()) % mod
                        cnt += 1
                    elif len(pos) >= 2 and pos[-1] * pos[-2] >= neg[-1]:
                        mul = (mul * pos.pop() * pos.pop()) % mod                            
                        cnt += 2
                    else:
                        mul = (mul * neg.pop()) % mod
                        cnt += 2                    
                elif pos:
                    mul = (mul * pos.pop()) % mod
                    cnt += 1
                elif neg:
                    assert cnt <= k - 2 and (k - cnt) % 2 == 0
                    mul = (mul * neg.pop()) % mod
                    cnt += 2
                else:
                    raise RuntimeError
            return mul

        elif zero_cnt != 0:
            # 答えは 0 にできる。0 が最善や
            return 0

        else:
            # 答えは負にしかならぬ。できるだけ 0 に近い負の値を作ろう
            tmp = [abs(elm) for elm in L]
            tmp.sort()
            mul = 1
            # print(tmp)
            for i in range(k):
                mul = (mul * tmp[i]) % mod
            return mod - mul
    
    
    n, k = mi()
    L = lmi()

    print(solve(n, k, L))




if __name__ == "__main__":
    main()
