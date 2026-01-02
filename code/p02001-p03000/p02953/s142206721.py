import glob

#IS_TEST = 1

# 問題ごとのディレクトリのトップからの相対パス
REL_PATH = 'ABC\\136\\C'

# テスト用ファイル置き場のトップ
TOP_PATH = 'C:\\AtCoder'

class Common:

    problem = []
    index = 0

    def __init__(self, rel_path):
        self.rel_path = rel_path

    def initialize(self, path):
        file = open(path)
        self.problem = file.readlines()
        self.index = 0
        return

    def input_data(self):
        try:
            IS_TEST
            self.index += 1
            return self.problem[self.index-1]

        except NameError:
            return input()

    def resolve(self):
        pass

    def exec_resolve(self):
        try:
            IS_TEST
            for path in glob.glob(TOP_PATH + '\\' + self.rel_path + '/*.txt'):
                self.initialize(path)
                self.resolve()
        except NameError:
            self.resolve()


class C(Common):

    def resolve(self):

        n = int(self.input_data())
        stairs = [int(i) for i in self.input_data().split()]
        now = 0

        for i in range(n):
            if stairs[i] < now:
                print('No')
                exit(0)
            if stairs[i] > now:
                stairs[i] -= 1
                now = stairs[i]

        print('Yes')

solver = C(REL_PATH)
solver.exec_resolve()