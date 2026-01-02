def zeroPadding(num):
    return "%06d"%num

def zeroPadding10(num):
    return "%010d"%num

class Row:
    def __init__(self, i, pref_id, year):
        self.i = i
        self.pref_id = pref_id
        self.year = year
        self.city_id = -1
        
    def __str__(self):
        return "{i: %d, pref_id: %d, year: %d, city_id: %d}"%(self.i, self.pref_id, self.year, self.city_id)
        
    def set_city_id(self, city_id):
        self.city_id = city_id
            
    def get_sort_key(self):
        return zeroPadding(self.pref_id ) + zeroPadding10(self.year) 
            
    def get_str(self):
        return zeroPadding(self.pref_id ) + zeroPadding(self.city_id)

N, M = map(int,input().split()) 

row_list = []

for i in range(M):
    d = list(map(int,input().split())) 
    row_list.append(Row(i, d[0], d[1]))

row_list = sorted(row_list, key=lambda x: x.get_sort_key())

now_pref_id = -1
cnt = 1

result = []
for i, row in enumerate(row_list):
    if row.pref_id != now_pref_id:
        now_pref_id = row.pref_id
        cnt = 1
    
    row.set_city_id(cnt)
    row_list[i] = row
    cnt += 1

[print(x.get_str()) for x in sorted(row_list, key=lambda x: x.i)]