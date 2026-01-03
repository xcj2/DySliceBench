class iostream:
    def __init__(self):
        self.s = []
        self.i = 0

    def next(self, T=str):
        if(self.i < len(self.s)):
            ret = self.s[self.i]
            self.i += 1
            return T(ret)
        st = input()
        while(st == ""):
            st = input()
        self.s = st.split(" ")
        self.i = 0
        return T(self.next(T))

def even(n):
    return n % 2 == 0

def main():
    cin = iostream()
    a, b, c = cin.next(int), cin.next(int), cin.next(int)
    if even(a) or even(b) or even(c):
        print(0)
        exit()
    a, b, c = sorted([a, b, c])
    print(a * b)


main()
