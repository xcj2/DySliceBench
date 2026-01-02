# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0301
# 双方向循環リストを使用した実装
from sys import stdin


class DoublyCicularList():

    class Cell():
        def __init__(self, v):
            self.next = None
            self.previous = None
            self.value = v

    def __init__(self):
        self.pos = DoublyCicularList.Cell(0)
        self.pos.next = self.pos
        self.pos.previous = self.pos
        self.head = self.pos


def main():
    N, M, Q = map(lambda x: int(x), stdin.readline().strip().split(' '))
    a_list = map(lambda x: int(x), stdin.readline().strip().split(' '))
    q_list = map(lambda x: int(x), stdin.readline().strip().split(' '))
    dcl = DoublyCicularList()
    for i in range(1, N):
        prev = dcl.pos
        dcl.pos.next = DoublyCicularList.Cell(i)
        dcl.pos = dcl.pos.next
        dcl.pos.previous = prev
        dcl.pos.next = dcl.head
        dcl.head.previous = dcl.pos
    dcl.pos = dcl.head
    for i, a in enumerate(a_list):
        for _ in range(a % (N-i)):
            if a % 2 == 0:
                dcl.pos = dcl.pos.next
            else:
                dcl.pos = dcl.pos.previous
        dcl.pos.previous.next = dcl.pos.next
        dcl.pos.next.previous = dcl.pos.previous
        dcl.pos = dcl.pos.next
    res_list = []
    last_value = dcl.pos.previous.value
    while True:
        if dcl.pos.value == last_value:
            res_list.append(dcl.pos.value)
            break
        res_list.append(dcl.pos.value)
        dcl.pos = dcl.pos.next
    print('\n'.join(['1' if q in res_list else '0' for q in q_list]))


if __name__ == '__main__':
    main()

