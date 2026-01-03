""" abc055_a """

import sys

H = pow(10, 9) + 7

def _main():
    _n = int(sys.stdin.readline())
    answers = list(map(lambda a: a == 'o', sys.stdin.readline()))

    # ooxoox
    # S-----
    # a[0] = o: SS---S
    # a[1] = o: SSS--S
    # a[2] = x: SSSW-S
    # a[3] = o: SSSWWS
    # a[4] = o: SSSWWS OK
    # a[5] = x: SSSWWS OK

    def _evaluate(zoo_first, zoo_last):

        zoo = [None] * _n

        zoo[0] = zoo_first == 'S'
        zoo[_n-1] = zoo_last == 'S'

        for i in range(0, _n):
            same = answers[i] if zoo[i] else not answers[i]
            next_z = zoo[(i-1)%_n] if same else not zoo[(i-1)%_n]
            if zoo[(i+1)%_n] is None:
                zoo[(i+1)%_n] = next_z
            else:
                if zoo[(i+1)%_n] != next_z:
                    return -1

        return zoo

    for _f, _l in [['S', 'S'], ['W', 'W'], ['S', 'W'], ['W', 'S'],]:
        result = _evaluate(_f, _l)
        if -1 != result:
            print(_format(result))
            return

    print(-1)

def _format(result):
    return ''.join(map(lambda e: 'S' if e else 'W', result))

if __name__ == '__main__':
    _main()
