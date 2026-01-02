def main():
    class MyClass:
        def __init__(self):
            self.strings = ""

        def rpl(self, int1, int2, str1):
            self.strings = self.strings[:int1] + str1 + self.strings[int2+1:]

        def rvr(self, int1, int2):
            if int1 >= 1:
                revstr = self.strings[int2:int1-1:-1]
            else:
                revstr = self.strings[int2::-1]
            self.strings = self.strings[:int1] + revstr + self.strings[int2+1:]

        def pri(self, int1, int2):
            print(self.strings[int1:int2+1])

    cls = MyClass()
    cls.strings = input()
    n = int(input())
    for _ in range(n):
        li = input().split()
        if li[0] == "replace":
            cls.rpl(int(li[1]), int(li[2]), li[3])
        elif li[0] == "reverse":
            cls.rvr(int(li[1]), int(li[2]))
        elif li[0] == "print":
            cls.pri(int(li[1]), int(li[2]))


if __name__ == "__main__":
    main()