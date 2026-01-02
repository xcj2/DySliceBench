from operator import attrgetter

class Robot:
  def __init__(self, position, length):
    self.position = position
    self.length = length

  @property
  def begin(self):
    return self.position - self.length
  
  @property
  def end(self):
    return self.position + self.length
  
  def __repr__(self):
    return '({0}, {1})'.format(self.begin, self.end)


N = int(input())

robots = []

for _ in range(N):
  x, l = map(int, input().split())
  robots.append(Robot(x, l))
  
robots.sort(key=attrgetter('end'))

selected = []

for robot in robots:
  if len(selected) < 1:
    selected.append(robot)
    continue

  if robot.begin >= selected[-1].end:
    selected.append(robot)
  
print(len(selected))