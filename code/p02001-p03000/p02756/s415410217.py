import sys
input = sys.stdin.readline
import collections

# 持っているビスケットを叩き、1枚増やす
# ビスケット A枚を 1円に交換する
# 1円をビスケット B枚に交換する
def main():
    s = input().strip()
    q = int(input())
    flg = True
    deq = collections.deque(s)
    for i in range(q):
        t = input_list_str()
        if len(t) == 1:
            n = t[0]
            flg = False if flg is True else True
        else:
            n, f, c = t
            c = str(c).strip()
            if f == '1':
                if flg:
                    deq.appendleft(c)
                else:
                    deq.append(c)
            else:
                if flg:
                    deq.append(c)
                else:
                    deq.appendleft(c)
    if flg is False:
        deq.reverse()
    print(''.join(deq))


def bi(num, a, b, x):
    print((a * num) + (b * len(str(b))))
    if (a * num) + (b * len(str(b))) <= x:
        return False
    return True

def input_list():
    return list(map(int, input().split()))


def input_list_str():
    return list(map(str, input().split()))


if __name__ == "__main__":
    main()
