if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    def parent(i):
        return i//2

    def left(i):
        return 2*i

    def right(i):
        return 2*i+1

    H = int(input())

    # 1オリジンにするために、0番目にNoneを入れておく
    A = [None] + list(map(int, input().split()))

    # 1オリジンでfor文回す
    for i in range(1, H+1):
        print('node ' + str(i) + ': ', end='')
        print('key = ' + str(A[i]) + ', ', end='')
        if 1 <= parent(i):
            print('parent key = ' + str(A[parent(i)]) + ', ', end='')
        if left(i) <= H:
            print('left key = ' + str(A[left(i)]) + ', ', end='')
        if right(i) <= H:
            print('right key = ' + str(A[right(i)]) + ', ', end='')
        print('')  # 改行のため

