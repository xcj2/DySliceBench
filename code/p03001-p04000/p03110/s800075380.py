#!/usr/bin/env python3
import sys

JPY = 'JPY'
BTC = 'BTC'
RAITO_BTC_TO_JPY = 380000
# 1.0 BTC == 380000.0 円

def solve(N: int, x: "List[float]", u: "List[str]"):
    #x_ = list(map(standardize_to_JPY, zip(x,u)))
    x_ = []
    for i in range(N):
        x_.append(standardize_to_JPY(x[i], u[i]))
    print(sum(x_))
    return

def standardize_to_JPY(xi, ui):
    if ui == BTC:
        return xi * RAITO_BTC_TO_JPY
    else:
        return xi

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    x = [float()] * (N)  # type: "List[float]" 
    u = [str()] * (N)  # type: "List[str]" 
    for i in range(N):
        x[i] = float(next(tokens))
        u[i] = next(tokens)
    solve(N, x, u)

if __name__ == '__main__':
    main()
