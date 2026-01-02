class Mod13DPTable:
    MOD = 10**9 + 7
    def __init__(self, length):
        self.mod13 = [{j:0 for j in range(13)} for i in range(length)]
        self.MOD = 10**7 + 7
    def set_start(self, units_digit):
        if units_digit == '?':
            for i in range(10):
                self.mod13[0][i] = 1
        else:
            self.mod13[0][int(units_digit)] = 1
    def get_table(self, digit):
        return self.mod13[digit]
    def update(self, num, digit, multi):  # multi = 10**digit % 13
        for k, v in self.mod13[digit-1].items():
            remain = ((num * multi) + k) % 13
            self.mod13[digit][remain] = (self.mod13[digit][remain] + v) % Mod13DPTable.MOD
            
def main():
    MOD = 10**9 + 7
    S = input()
    mod13dp = Mod13DPTable(len(S))
    mod13dp.set_start(S[-1])
    multi = 10
    for i, m in enumerate(reversed(list(S[:-1]))):
        i += 1
        if m == '?':
            for j in range(10):
                mod13dp.update(j, i, multi)
        else:
            mod13dp.update(int(m), i, multi)
        multi = multi*10 % 13
    print(mod13dp.get_table(-1)[5])
main()