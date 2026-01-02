def mapt(fn, *args):
    return list(map(fn, *args))

def Array(listseq):
    return mapt(Vector, listseq)

def Vector(line):
    return mapt(Atom, line.split(" "))

def Atom(segment):
    try:
        return int(segment)
    except ValueError:
        try:
            float(segment)
        except ValueError:
            return segment


def parse_second(rest):
    first, end, strings = rest[0], rest[1], rest[-1]
    return first, end+1, strings


def main(word, orders):
    parsed =Array(orders)
    word = list(word)
    for cmd, *rest in parsed:
        first, end, strings = parse_second(rest)

        if    cmd == "replace": word[first:end] = strings
        elif  cmd == "reverse": word[first:end] = reversed(word[first:end])
        else: print("".join(word[first:end]))



word = input()
times = int(input())
orders = [input() for _ in range(times)]
main(word, orders)
