class Stack:
    def __init__(self, full_idx=10):
        self.stack = [None] * full_idx
        self.top = 0
        self.MAX = full_idx

    def is_empty(self):
        return self.top == 0

    def is_full(self):
        return self.top >= self.MAX - 1

    def push(self, x):
        if self.is_full():
            raise IndexError

        self.top += 1
        self.stack[self.top] = x

    def pop(self):
        if self.is_empty():
            raise IndexError

        self.top -= 1
        return self.stack[self.top+1]


def main():
    s = input()
    s1, s2 = Stack(20000), Stack(20000)
    pond = [0]
    area = 0

    for i in range(len(s)):
        if s[i] == "\\":
            s1.push(i)
            s2.push([i, 0])

        elif s[i] == "/":
            if not s1.is_empty():
                area += i - s1.pop()
            if not s2.is_empty():
                tup = s2.pop()
                area2 = 0

                while tup[1] != 0:
                    tup2 = s2.pop()
                    tup, tup2 = tup2, tup
                    area2 += tup2[1]

                tup[1] = i - tup[0] + area2

                if s2.is_empty():
                    pond.append(tup[1])
                else:
                    s2.push(tup)

    s3 = Stack(20000)
    while not s2.is_empty():
        ss = s2.pop()
        if ss[1] != 0:
            s3.push(ss)

    while not s3.is_empty():
        pond.append(s3.pop()[1])

    pond[0] = len(pond) - 1
    print(area)
    print(" ".join([str(i) for i in pond]))


if __name__ == '__main__':
    main()

