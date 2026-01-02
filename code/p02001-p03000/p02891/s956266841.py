import sys
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
INF = 10 ** 18
MOD = 10 ** 9 + 7

# debug = True
debug = False

def dprint(*objects):
    if debug == True:
        print(*objects)

def solve():
    S = SI()
    K = II()
    N = len(S)

    same_cnt = 0
    for c in S:
        if c == S[0]:
            same_cnt += 1

    if same_cnt == N:
        print((N*K)//2)
        return

    chunks = []
    prev = ''
    chunk_len = 0
    in_chunk = False
    for i, c in enumerate(S):
        dprint(c, in_chunk, prev, c)
        if prev == c:
            if in_chunk:
                chunk_len += 1
            else:
                chunk_len = 2
                chunk_start = i-1
                in_chunk = True
        else:
            if in_chunk:
                in_chunk = False
                chunks.append((chunk_start, chunk_len))
        prev = c

    if in_chunk:
        chunks.append((chunk_start, chunk_len))

    # start end chunk
    if S[0] == S[N-1]:
        start_chunk_head = chunks[0][0]
        end_chunk_tail = chunks[len(chunks)-1][0] + chunks[len(chunks)-1][1] - 1
        start_n, end_n = 1, 1
        start_chunk_i = 0
        cnt_for_end_chunk = 0
        cnt_for_start_chunk = 0
        end_chunk_i = len(chunks) - 1
        if start_chunk_head == 0:
            start_n = chunks[0][1]
            start_chunk_i = 1
            cnt_for_start_chunk = start_n // 2
        if end_chunk_tail == N-1:
            end_n = chunks[len(chunks)-1][1]
            end_chunk_i = len(chunks) - 2
            cnt_for_end_chunk = end_n // 2

        start_end_chunk_n = start_n + end_n

        dprint(chunks, start_n, end_n, start_end_chunk_n)
        dprint(start_chunk_i, end_chunk_i)
        cnt = 0
        for chead, clen in chunks[start_chunk_i:end_chunk_i+1]:
            cnt += clen //2
        dprint(cnt)
        cnt = cnt*K + start_end_chunk_n//2 * (K-1) + cnt_for_end_chunk + cnt_for_start_chunk

        print(cnt)
        return


    else:
        cnt = 0
        for chead, clen in chunks:
            cnt += clen //2
        print(cnt * K)
        return


solve()