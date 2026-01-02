import logging
from collections import Counter
import math

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def P(n, r):
    return math.factorial(n)//math.factorial(n-r)

def C(n, r):
    return P(n, r)//math.factorial(r)

def main():
    N = int(input())
    S_ = ["".join(sorted(list(input()))) for _ in range(N)]
    
    logging.info(S_)

    counters = dict(Counter(S_))

    logging.info(counters)
    
    ans = 0
    for key, val in counters.items():
        if val != 1:
            ans += C(val, 2)

    print(ans)
    
    
if __name__ == "__main__":
    main()
