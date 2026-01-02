
class Dice:
    def __init__(self, v1, v2, v3, v4, v5, v6):
        self.faces = [(v1, v6), (v2, v5), (v3, v4)]

    def rotate_left(self):
        (top, btm), (fnt, bck), (rgt, lft) = self.faces
        return self.__class__(top, rgt, bck, fnt, lft, btm)

    def rotate_right(self):
        (top, btm), (fnt, bck), (rgt, lft) = self.faces
        return self.__class__(top, lft, fnt, bck, rgt, btm)

    def turn_back(self):
        (top, btm), (fnt, bck), (rgt, lft) = self.faces
        return self.__class__(fnt, btm, rgt, lft, top, bck)

    def turn_front(self):
        (top, btm), (fnt, bck), (rgt, lft) = self.faces
        return self.__class__(bck, top, rgt, lft, btm, fnt)

    def turn_right(self):
        (top, btm), (fnt, bck), (rgt, lft) = self.faces
        return self.__class__(lft, fnt, top, btm, bck, rgt)

    def turn_left(self):
        (top, btm), (fnt, bck), (rgt, lft) = self.faces
        return self.__class__(rgt, fnt, btm, top, bck, lft)

    def __hash__(self):
        (top, btm), (fnt, bck), (rgt, lft) = self.faces
        return hash(frozenset((frozenset((top, btm)),
                               frozenset((fnt, bck)),
                               frozenset((rgt, lft)))))

    def __str__(self):
        return "<{}>".format(",".join([str(t) for t in self.faces]))

    def __eq__(self, other):
        def equals(d1, d2):
            return d1.faces == d2.faces

        (top, btm) = self.faces[0]
        if (top, btm) in other.faces:
            return (equals(self, other)
                    or equals(self.rotate_right(), other)
                    or equals(self.rotate_left(), other)
                    or equals(self.turn_right(), other)
                    or equals(self.turn_front(), other)
                    or equals(self.rotate_left().rotate_left(), other)
                    or equals(self.turn_back().rotate_left(), other)
                    or equals(self.turn_front().rotate_right(), other)
                    or equals(self.turn_right().rotate_left(), other)
                    or equals(self.turn_left().rotate_right(), other)
                    or equals(self.turn_right().turn_back().turn_back(),
                              other)
                    or equals(self.turn_front().turn_right().turn_right(),
                              other))
        elif (btm, top) in other.faces:
            return self.turn_front().turn_front() == other
        else:
            return False


def run():
    count = int(input())
    dices = set()

    for _ in range(count):
        dice = Dice(*[int(i) for i in input().split()])
        if dice in dices:
            print("No")
            break
        dices.add(dice)
    else:
        print("Yes")


if __name__ == '__main__':
    run()

