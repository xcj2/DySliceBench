import functools
import heapq


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

    N, K = read_int_array()
    nums = read_int_array()
    ans = 0

    @functools.lru_cache(None)
    def dp(i, j, handsum):
        nonlocal ans
        left = j + 1 - i
        taken = N - left
        if taken == K:
            ans = max(ans, handsum)
            return
        moves = K - taken

        if i <= j:
            dp(i+1, j, handsum + nums[i])
            dp(i, j-1, handsum + nums[j])

        can_return = sum(sorted([x for x in (nums[:i] + nums[j+1:]) if x < 0])[:moves])
        ans = max(ans, handsum - can_return)

    dp(0, N-1, 0)
    write(ans)

main()
