class C:
    def __init__(self):
        self.value = []
    def append(self, n):
        self.value.append(n)

    def popleft(self):
        if not self.value:
            return -1
        else:
            ret = self.value[0]
            del self.value[0]
            return ret
    def popover(self, n):
        ret = -1
        for i, v in enumerate(self.value):
            if v > n:
                ret = v
                del self.value[i]
                break
        return ret

    def empty(self):
        return self.value == []

    @property
    def length(self):
        return len(self.value)

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        taro_bool = [False] * (2 * n + 1)
        taro = C()
        hanako = C()
        for i in range(n):
            v = int(input())
            taro_bool[v] = True
        for i in range(1, 2 * n + 1):
            if taro_bool[i]:
                taro.append(i)
            else:
                hanako.append(i)
                
        ba = taro.popleft()
        teban = 1 # 0太郎 1花子
        playing = [taro, hanako]
        while not taro.empty() and not hanako.empty():
            if ba == 0:
                ba = playing[teban].popleft()
            else:
                x = playing[teban].popover(ba)
                ba = x if x > 0 else 0
            teban ^= 1
    
        print(hanako.length)
        print(taro.length)


if __name__ == '__main__':
    main()


