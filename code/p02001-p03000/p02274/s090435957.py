
import sys

sys.setrecursionlimit(10 ** 7)
read = sys.stdin.buffer.read
inp = sys.stdin.buffer.readline


def inpS(): return inp().rstrip().decode()


readlines = sys.stdin.buffer.readlines
MOD = 10 ** 9 + 7
INF = 1 << 60

# ---------------------------------------------------
# ---------------------------------------------------
# ---------------------------------------------------

cnt = 0
def resolve():
    def merge(l, r):
        global cnt
        mA = []
        l_i = 0
        r_i = 0
        while l_i < len(l) and r_i < len(r):
            if l[l_i] <= r[r_i]:
                mA.append(l[l_i])
                l_i += 1
            else:
                mA.append(r[r_i])
                r_i += 1
                # Lの個数から今のL_indを引けばRより大きい個数がわかる
                cnt += len(l) - l_i
        # 残りを加える
        if l_i < len(l):
            mA.extend(l[l_i:])
        elif r_i < len(r):
            mA.extend(r[r_i:])
        return mA

    def mergesort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = mergesort(arr[:mid])
        right = mergesort(arr[mid:])

        return merge(left, right)

    N = int(inp())
    A = list(map(int, inp().split()))

    mergesort(A)
    print(cnt)

if __name__ == '__main__':
    resolve()
