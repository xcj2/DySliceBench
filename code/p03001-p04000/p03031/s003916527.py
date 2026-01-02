def main():
    from sys import stdin, stdout

    def read():
        return stdin.readline().rstrip('\n')

    def read_array(sep=None, maxsplit=-1):
        return read().split(sep, maxsplit)

    def read_int():
        return int(read())

    def read_int_array(sep=None, maxsplit=-1):
        return [int(a) for a in read_array(sep, maxsplit)]

    def write(*args, **kwargs):
        sep = kwargs.get('sep', ' ')
        end = kwargs.get('end', '\n')
        stdout.write(sep.join(str(a) for a in args) + end)

    def write_array(array, **kwargs):
        sep = kwargs.get('sep', ' ')
        end = kwargs.get('end', '\n')
        stdout.write(sep.join(str(a) for a in array) + end)

    N, M = read_int_array()
    bulbs = [None]*M
    for i in range(M):
        k, *switches = read_int_array()
        bulbs[i] = switches
    P = read_int_array()
    switches = []
    ans = 0
    def build(i):
        nonlocal ans
        if i == N:
            if all(sum(switches[x-1] for x in bulbs[i]) % 2 == P[i] for i in range(M)):
                ans += 1
        else:
            switches.append(False)
            build(i+1)
            switches[-1] = True
            build(i+1)
            switches.pop()
    build(0)
    write(ans)

main()
