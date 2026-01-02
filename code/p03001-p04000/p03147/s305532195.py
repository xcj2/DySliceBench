
import numpy as np

class MyClass:
    def __init__(self):
        self.sum = 0

    def water(self, H):
        if len(H)<=0:
            return
        min_h = np.min(H)
        self.sum += min_h
        H -= min_h
        on = False
        for i in range(len(H)):
            if not on:
                if H[i]>0:
                    st = i
                    on = True
                else:
                    continue
            else:
                if H[i]>0:
                    continue
                else:
                    ed = i
                    on = False
                    self.water(H[st:ed])
        if on:
            self.water(H[st:])
        return


def main():
    N = int(input())
    H = np.array([int(x) for x in input().split()]) # Length of N
    my_class = MyClass()
    my_class.water(H)
    print(my_class.sum)

if __name__=='__main__':
    main()