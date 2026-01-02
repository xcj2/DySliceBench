class Rectangle(object):
    def __init__(self, length:int, breadth:int) -> None:
        if length < 1:
            raise ValueError('Paramter length is lower than 1.')
        if length > 100:
            raise ValueError('Paramter length is larger than 100.')
        if breadth < 1:
            raise ValueError('Paramter breadth is lower than 1.')
        if breadth > 100:
            raise ValueError('Paramter breadth is larger than 100.')

        self.length = length
        self.breadth = breadth

    def get_area(self) -> int:
        return self.length * self.breadth

    area = property(get_area)

    def get_perimeter(self) -> int:
        return 2 * (self.length + self.breadth)

    perimeter = property(get_perimeter)

if __name__ == "__main__":
    in_str = input()
    param = in_str.split()
    length = int(param[0])
    breadth = int(param[1])

    rect = Rectangle(length, breadth)
    print('{0} {1}'.format(rect.area, rect.perimeter))

