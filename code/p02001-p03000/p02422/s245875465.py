class StringEditor:
    def __init__(self, s):
        self.s = s

    def __str__(self):
        return self.s

    def print(self, start, end):
        """print command

        >>> e = StringEditor('abcde')
        >>> e.print(1, 3)
        bcd
        """
        print(self.s[start:end+1])

    def replace(self, start, end, word):
        """replace command

        >>> e = StringEditor('abcde')
        >>> e.replace(1, 3, 'xyz')
        >>> e.print(0, 4)
        axyze
        """
        self.s = self.s[:start] + word + self.s[end+1:]

    def reverse(self, start, end):
        """reverse command

        >>> e = StringEditor('abcde')
        >>> e.reverse(0, 2)
        >>> e.print(0, 4)
        cbade
        >>> e.reverse(2, 3)
        >>> e.print(0, 4)
        cbdae
        """
        if start > 0:
            rev = self.s[end:start-1:-1]
        else:
            rev = self.s[end::-1]

        self.s = self.s[:start] + rev + self.s[end+1:]


def run():
    s = input()
    num = int(input())
    editor = StringEditor(s)

    for _ in range(num):
        com, *args = input().split()

        if com == 'print':
            start, end = [int(i) for i in args]
            editor.print(start, end)
        elif com == 'reverse':
            start, end = [int(i) for i in args]
            editor.reverse(start, end)
        elif com == 'replace':
            start, end = [int(i) for i in args[0:2]]
            word = args[-1]
            editor.replace(start, end, word)
        else:
            raise ValueError('invalid command')


if __name__ == '__main__':
    run()
