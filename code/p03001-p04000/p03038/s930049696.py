from heapq import *

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

    n, m = read_int_array()
    nums = read_int_array()

    heapify(nums)
    ops = [None]*m
    for i in range(m):
        b, c = read_int_array()
        ops[i] = (c, b)
    ops.sort(reverse=True)

    done = []
    for c, b in ops:
        while b and nums and nums[0] < c:
            heappop(nums)
            done.append(c)
            b -= 1
        if not nums or nums[0] >= c:
            break
    write(sum(nums) + sum(done))

main()
