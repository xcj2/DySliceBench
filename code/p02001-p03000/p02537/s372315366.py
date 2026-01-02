import sys
input = sys.stdin.readline
N, K = map(int, input().rstrip().split())

BL = (300001-1).bit_length()
WIDTH = pow(2, BL)
BUFSIZE = pow(2, BL+1) - 1
BASE = BUFSIZE - WIDTH
DEFAULT = 0

buf = [DEFAULT] * BUFSIZE

def update(i, x):
    i += BASE
    buf[i] = x
    i = (i-1) // 2
    while i >= 0:
        buf[i] = compare(buf[2*i+1], buf[2*i+2])
        i = (i-1) // 2

# [q_left, q_right]
def search(left, right):
    ansl = ansr = DEFAULT
    left += BASE
    right += BASE
    while left < right:
        if not (left & 1):
            ansl = compare(ansl, buf[left])
            left += 1
        if right & 1:
            ansr = compare(ansr, buf[right])
            right -= 1
        left = (left-1) // 2
        right = (right-1) // 2
    if left == right:
        ansl = compare(ansl, buf[left])
    return compare(ansl, ansr)

def compare(v1, v2):
    return v1 if v1 > v2 else v2

for _ in range(N):
    a = int(input().rstrip())
    maxlen = search(max(0, a-K), min(a+K, 300000))
    update(a, maxlen+1)
print(search(0, 300000))
