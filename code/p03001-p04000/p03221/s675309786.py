class City:
  def __init__(self, born):
    self.born = born
    self.id = ''

class Pref:
  def __init__(self, id):
    self.id = str(id).zfill(6)
    self.cities = []
  
  def add_city(self, city):
    self.cities.append(city)
  
  def issue_ids(self):
    self.cities.sort(key=lambda c:c.born)
    for i, c in enumerate(self.cities):
      c.id = self.id + str(i+1).zfill(6)

      
prefs = dict()
cities = []
n, m = map(int, input().split())
for _ in range(m):
  p, y = map(int, input().split())
  city = City(y)
  cities.append(city)
  if p in prefs:
    prefs[p].add_city(city)
  else:
    pref = Pref(p)
    pref.add_city(city)
    prefs[p] = pref

for p in prefs.values():
  p.issue_ids()

for c in cities:
  print(c.id)
