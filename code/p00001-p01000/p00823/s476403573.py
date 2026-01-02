# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1244
from typing import List, Dict

atomic_table: Dict[str, int] = {}


class NoAppearAtomicSymbol(Exception):
    pass


class Token:
    s: str
    index = 0

    def __init__(self, s: str):
        self.s = s

    @property
    def c(self) -> str:
        assert self.ok
        return self.s[self.index]

    @property
    def ok(self) -> bool:
        return self.index < len(self.s)

    def next(self):
        self.index += 1


def molecule(t: Token) -> int:
    n = 0
    while t.ok:
        if t.c == '(':
            t.next()
            m = molecule(t)
            t.next()
            m *= number(t)
            n += m
        elif t.c == ')':
            break
        else:
            m = atom(t)
            m *= number(t) or 1
            n += m
    return n


def atom(t: Token) -> int:
    c = ''
    if t.c.isupper():
        c += t.c
        t.next()
    if t.ok and t.c.islower():
        c += t.c
        t.next()
    try:
        return atomic_table[c]
    except KeyError:
        raise NoAppearAtomicSymbol


def number(t: Token) -> int:
    n = 0
    while t.ok and t.c.isdigit():
        n = n * 10 + int(t.c)
        t.next()
    return n


def readuntil(sep: str) -> List[str]:
    lines = []
    while True:
        line = input()
        if line == sep:
            break
        lines.append(line)
    return lines


def main():
    global atomic_table

    atoms = [l.split() for l in readuntil('END_OF_FIRST_PART')]
    atomic_table = {k: int(v) for (k, v) in atoms}
    for seq in readuntil('0'):
        try:
            print(molecule(Token(seq)))
        except NoAppearAtomicSymbol:
            print('UNKNOWN')


main()

