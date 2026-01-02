import builtins
import functools
import sys
import textwrap
from io import StringIO


def solve(input, print):
    A, B, C, X, Y = map(int, input().split())

    cost_min = sys.maxsize
    for c in range(max([X, Y]) + 1):
        cost = c * 2 * C
        a = X - c
        b = Y - c
        if a > 0:
            cost += a * A
        if b > 0:
            cost += b * B
        cost_min = min([cost_min, cost])
    print(cost_min)


if __name__ == '__main__':
    solve(builtins.input, functools.partial(builtins.print, flush=True))


def make_input(s):
    ss = textwrap.dedent(s).splitlines()
    it = iter(ss)
    return functools.partial(next, it)


def execute_solve(input_text):
    result = StringIO()
    solve(make_input(input_text),
          functools.partial(print, file=result, flush=True))
    return result.getvalue()


def test_solve():
    assert execute_solve('1500 2000 1600 3 2') == '7900\n'
    assert execute_solve('1500 2000 1900 3 2') == '8500\n'
    assert execute_solve('1500 2000 500 90000 100000') == '100000000\n'
