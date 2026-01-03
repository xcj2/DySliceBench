import sys


def solve(sx: int, sy: int, tx: int, ty: int):
    print("U"*(ty-sy)+"R"*(tx-sx)+"D"*(ty-sy)+"L"*(tx-sx)+"L"+"U"*(ty-sy+1)+"R"*(tx-sx+1)+"D"+"R"+"D"*(ty-sy+1)+"L"*(tx-sx+1)+"U")
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    sx = int(next(tokens))  # type: int
    sy = int(next(tokens))  # type: int
    tx = int(next(tokens))  # type: int
    ty = int(next(tokens))  # type: int
    solve(sx, sy, tx, ty)

if __name__ == '__main__':
    main()
