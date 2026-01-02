class Cell:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num
        self.opened = False

    def open(self) -> None:
        self.opened = True

    def punch(self, called_number: int) -> None:
        if called_number == self.num:
            self.open()


class Line:
    """タテ・ヨコ・ナナメいずれかのライン"""

    def __init__(self, values):
        self.values = values

    def __post_init__(self):
        # 気分で書いたけど、今回はなくても良いと思う
        if len(self.values) != 3:
            raise ValueError('今回は3つ以外ありえないよ〜')

    def is_bingo(self) -> bool:
        return all([c.opened for c in self.values])


class Cells:
    """Boardって概念もあると思うけど、単純にCellのコレクションでいく"""

    def __init__(self, values):
        self.values = values

    def punch(self, called_numbers) -> None:
        for called_number in called_numbers:
            for cell in self.values:
                cell.punch(called_number)

    def has_one_more_bingo(self) -> bool:
        # タテ
        tate1 = Line([c for c in self.values if c.y == 1])
        tate2 = Line([c for c in self.values if c.y == 2])
        tate3 = Line([c for c in self.values if c.y == 3])

        # ヨコ
        yoko1 = Line([c for c in self.values if c.x == 1])
        yoko2 = Line([c for c in self.values if c.x == 2])
        yoko3 = Line([c for c in self.values if c.x == 3])

        # ナナメ
        # 左上から右下に向かってのナナメ(＼)
        diag1 = Line([c for c in self.values if c.x == c.y])

        # 右上から左下に向かってのナナメ(／)
        diag2 = Line([c for c in self.values if (((c.x, c.y) == (1, 3)) or
                                                 ((c.x, c.y) == (2, 2)) or
                                                 ((c.x, c.y) == (3, 1)))])

        return any([tate1.is_bingo(), tate2.is_bingo(), tate3.is_bingo(),
                    yoko1.is_bingo(), yoko2.is_bingo(), yoko3.is_bingo(),
                    diag1.is_bingo(), diag2.is_bingo()])

    @classmethod
    def create(cls, A):
        cells = []

        for row, line in enumerate(A, start=1):
            for col, num in enumerate(line, start=1):
                cell = Cell(x=row, y=col, num=num)
                cells.append(cell)

        return Cells(cells)


def actual(n, A, B):
    cells = Cells.create(A)

    cells.punch(B)

    if cells.has_one_more_bingo():
        return 'Yes'

    return 'No'

line1 = list(map(int, input().split()))
line2 = list(map(int, input().split()))
line3 = list(map(int, input().split()))

A = [line1,
     line2,
     line3]

n = int(input())
B = []

for _ in range(n):
	b = int(input())
	B.append(b)
    

print(actual(n, A, B))