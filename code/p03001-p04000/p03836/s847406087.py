def main():
    sx, sy, tx, ty = map(int, input().split())

    tx = tx - sx
    ty = ty - sy

    def f1():
        s = ""
        s = s + "U" * ty
        s = s + "R" * tx
        return s

    def b1():
        s = ""
        s = s + "D" * ty
        s = s + "L" * tx
        return s

    def f2():
        s = ""
        s = s + "L" + "U" * (ty + 1)
        s = s + "R" * (tx + 1) + "D"
        return s

    def b2():
        s = ""
        s = s + "R" + "D" * (ty + 1)
        s = s + "L" * (tx + 1) + "U"
        return s

    print(f1() + b1() + f2() + b2())


if __name__ == "__main__":
    main()