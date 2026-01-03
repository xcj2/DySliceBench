# At BC 042 C (300)

# find first digit (from the left)
# that needs to be changed.
# if that digit is incremented, then
#   decrement everything after it as much as possible
# if that digit has to be decremented, then increase (or insert) a digit
#   before that digit and then decrement everything after the incremented digit
#
def dec(i, D):
    for k in range(i - 1, -1, -1):
        if k not in D:
            return k
    return i

def inc(i, D):
    for k in range(i + 1, 10):
        if k not in D:
            return k
    return i

def max_dec_or_inc(A, start, D):
    for j in range(start, len(A)):
        d = dec(A[j], D)
        if d != A[j]:
            while d != A[j]:
                A[j] = d
                d = dec(A[j], D)
        elif A[j] in D: # must change
            u = inc(i, D)
            A[j] = u

def inc_one(A, end, D):
    for j in range(end - 1, -1, -1):
        up = inc(A[j], D)
        if up != A[j]:
            A[j] = up
            return j
    A.insert(0, inc(0, D))
    return 0

def f(n, D):
    out = list(map(int, str(n)))
    for j, i in enumerate(out):
        if i in D: # first from left that needs to be changed
            up = inc(i, D)
            if up != i: # possible to increment at j
                out[j] = up
                # decrement everything after j
                max_dec_or_inc(out, j + 1, D)
            else: # must decrement at index j
                out[j] = dec(i, D)
                # increment one before j
                idx = inc_one(out, j, D)
                # decrement everything after j
                max_dec_or_inc(out, idx + 1, D)
            break
    r = int("".join([str(x) for x in out]))
    return r

assert f(1000, [1, 3, 4, 5, 6, 7, 8, 9]) == 2000
assert f(9999, [0]) == 9999
assert f(6888, [8, 9]) == 7000
assert f(9999, [9]) == 10000
assert f(9999, [0, 9]) == 11111
assert f(9999, [0, 1, 9]) == 22222

n, k = map(int, input().split())
D = list(sorted(map(int, input().split())))
ans = f(n, D)
print(ans)
