def get_input_data():
    input_data = int(input())
    return input_data

def get_two_data():
    two_data = input().split()
    for i in range(2):
        two_data[i] = int(two_data[i])
    return two_data

def make_gem_map(gem_num):
    gem_map = set()
    for i in range(gem_num):
        gem_map.add(tuple(get_two_data()))
    return gem_map

def make_order(order_num):
    order = [None] * order_num
    for i in range(order_num):
        order[i] = input().split()
        order[i][1] = int(order[i][1])
    return order

class Robot:

    def __init__(self, gem_map, order):
        self.x, self.y = (10, 10)
        self.gem_map = gem_map
        self.order = order

    def move_and_catch_gems(self):
        self.gem_map.discard((self.x, self.y))
        for i in range(len(order)):
            direction, vector = order[i]
            for j in range(vector):
                if direction == "N":
                    self.y += 1
                elif direction == "S":
                    self.y -= 1
                elif direction == "E":
                    self.x += 1
                else:
                    self.x -= 1
                self.gem_map.discard((self.x, self.y))

if __name__ == "__main__":
    while True:
        gem_num = get_input_data()
        if gem_num == 0:
            break
        gem_map = make_gem_map(gem_num)
        order_num = get_input_data()
        order = make_order(order_num)
        robot = Robot(gem_map, order)
        robot.move_and_catch_gems()
        if robot.gem_map:
            print("No")
        else:
            print("Yes")

