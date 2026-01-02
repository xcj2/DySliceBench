class Room:
  def __init__(self):
    self.__count = 0
  
  @property
  def count(self):
      return self.__count

  @count.setter
  def count(self, count):
      self.__count += count

class Floor:
  def __init__(self):
    self.__rooms = [Room() for i in range(10)]
  
  def room(self, i):
    return self.__rooms[i - 1]
  
  @property
  def get(self):
    return ' ' + ' '.join([str(self.__rooms[i].count) for i in range(10)])

class Building:
  def __init__(self):
    self.__floors = [Floor() for i in range(3)]
  
  def floor(self, i):
    return self.__floors[i - 1]
  
  @property
  def get(self):
    return '\n'.join([self.__floors[i].get for i in range(3)])

class School:
  def __init__(self):
    self.__buildings = [Building() for i in range(4)]
  
  def building(self, i):
    return self.__buildings[i - 1]
  
  @property
  def get(self):
    delimiter = '\n' + '#' * 20 + '\n'
    return delimiter.join([self.__buildings[i].get for i in range(4)])

if __name__ == '__main__':
  school = School()
  for i in range(int(input())):
     b, f, r, v = map(int, input().split())
     school.building(b).floor(f).room(r).count = v
  print(school.get)

