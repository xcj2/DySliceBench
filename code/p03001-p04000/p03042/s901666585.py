import copy

class Solver:
    def __init__(self, _s):
        self.prefix = _s[0:2]
        self.suffix = _s[2:4]

        self.solve()
    
    def solve(self):
        isPrefixYY = False
        isPrefixMM = False
        isSuffixYY = False
        isSuffixMM = False

        intPrefix = int(self.prefix)
        intSuffix = int(self.suffix)

        if intPrefix >= 1 and intPrefix <= 12:
            isPrefixMM = True
        if intSuffix >= 1 and intSuffix <= 12:
            isSuffixMM = True
        if intPrefix >= 0 and intPrefix <= 99:
            isPrefixYY = True
        if intSuffix >= 0 and intSuffix <= 99:
            isSuffixYY = True

        if isPrefixMM == True and isPrefixYY == True and isSuffixMM == True and isSuffixYY == True:
            print("AMBIGUOUS")
        elif isPrefixMM == True and isSuffixYY == True:
            print("MMYY")
        elif isPrefixYY == True and isSuffixMM == True:
            print("YYMM")
        else:
            print("NA")

def main():
    s=input()
    Solver(s)



if __name__ == "__main__":
    main()