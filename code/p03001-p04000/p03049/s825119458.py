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

    n = read_int()
    b_starts = 0
    a_ends = 0
    both = 0
    count = 0

    for i in range(n):
        word = read().strip()
        for i in range(1, len(word)):
            if word[i-1] == 'A' and word[i] == 'B':
                count += 1

        if word[0] == 'B' and word[-1] == 'A':
            both += 1
        elif word[-1] == 'A':
            a_ends += 1
        elif word[0] == 'B':
            b_starts += 1

    if a_ends > 0 and b_starts > 0:
        count += both + 1
        a_ends -= 1
        b_starts -= 1
    elif a_ends > 0:
        count += both
        a_ends -= 1
    elif b_starts > 0:
        count += both
        b_starts -= 1
    elif both:
        count += both - 1
    count += min(a_ends, b_starts)

    write(count)

main()
