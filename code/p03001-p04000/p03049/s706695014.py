import re

class Solver:
    def __init__(self, num):
        self.n = num
        self.ans = 0

        # Case 0: 文字列中にABが含まれている
        self.case_0 = 0

        # Case 1: 文字列が"B***A"
        self.case_1 = 0

        # Case 2: 文字列が"B***-"
        self.case_2 = 0

        # Case 3: 文字列が"-***A"
        self.case_3 = 0

        # Case 4: 文字列が"-***-"
        # そもそもカウントする必要がない
        # self.case_4 = 0

        self.solve()
    
    def solve(self):
        for i in range(self.n):
            sen = input()
            if sen.find("AB") != -1:
                for m in re.finditer(r"AB", sen):
                    self.case_0 = self.case_0 + 1
            if sen[0] == "B" and sen[-1] == "A":
                self.case_1 = self.case_1 + 1
            elif sen[0] == "B" and sen[-1] != "A":
                self.case_2 = self.case_2 + 1
            elif sen[0] != "B" and sen[-1] == "A":
                self.case_3 = self.case_3 + 1
    

        if self.case_1 == 0:
            self.ans = self.ans + min(self.case_3, self.case_2)
        else:
            if self.case_3 + self.case_2 > 0:
                self.ans = self.ans + self.case_1 + min(self.case_3, self.case_2)
            elif self.case_3 + self.case_2 == 0:
                self.ans = self.ans + self.case_1 - 1

        self.ans = self.ans + self.case_0

        print(str(self.ans))

def main():
    n=int(input())
    Solver(n)



if __name__ == "__main__":
    main()