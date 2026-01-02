import fileinput


def gcd(a, b):
    if b == 0:
        r = a
    else:
        r = gcd(b, a % b)
    return r


def gcdl(l):
    r = gcd(l[0], l[1])
    for i in range(2, len(l)):
        r = gcd(r, l[i])
    return r


def algorithm(n, a):
    return gcdl(a)


def pass_inputs(input_lines):
    n = input_lines[0][0]
    return algorithm(n, input_lines[1])


def convert_int(s):
    try:
        r = int(s)
    except ValueError:
        r = s
    return r


def run():
    out = pass_inputs([[convert_int(v) for v in l.strip().split(" ")] for l in fileinput.input()])
    print(out)


if __name__ == "__main__":
    run()
