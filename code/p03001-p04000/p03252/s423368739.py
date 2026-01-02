def char_range(c1, c2):
    """
    Generates the characters from `c1` to `c2`, inclusive.
    Taken from: https://stackoverflow.com/questions/7001144/range-over-character-in-python
    """
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

class Solver(object):
    def __init__(self):
        self.s = input()
        self.t = input()

    def solve(self):
        self.s_to_t = {}
        self.t_to_s = {}
        for c in char_range('a', 'z'):
            self.s_to_t[c] = None
            self.t_to_s[c] = None
        
        for i in range(len(self.s)):
            cs = self.s[i]
            ct = self.t[i]
            if self.s_to_t[cs] is None:
                self.s_to_t[cs] = ct
            if self.t_to_s[ct] is None:
                self.t_to_s[ct] = cs
            if self.s_to_t[cs] != ct:
                print("No")
                return
            if self.t_to_s[ct] != cs:
                print("No")
                return
        print("Yes")


if __name__ == "__main__":
    s = Solver()
    s.solve()