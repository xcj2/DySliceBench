class Dice:
    def __init__(self, labels):
        self.labels = labels
        
    def __str__(self):
        return str(self.labels[0])
    
    def roll_south(self):
        self.labels[0], self.labels[1], self.labels[5], self.labels[4] = self.labels[4], self.labels[0], self.labels[1], self.labels[5]
            
    def roll_east(self):
        self.labels[0], self.labels[2], self.labels[5], self.labels[3] = self.labels[3], self.labels[0], self.labels[2], self.labels[5]
    
    def roll_west(self):
        self.labels[0], self.labels[3], self.labels[5], self.labels[2] = self.labels[2], self.labels[0], self.labels[3], self.labels[5]
    
    def roll_north(self):
        self.labels[0], self.labels[4], self.labels[5], self.labels[1] = self.labels[1], self.labels[0], self.labels[4], self.labels[5]
        
    def get_faces(self):
        return self.labels
        
def main():
    labels0 = list(map(int, input().split()))
    labels = list(map(int, input().split()))
    d = Dice(labels)
    
    d0 = Dice(labels0)
    f = labels0[0]
    for i in labels0:
        if labels0.count(i) < labels0.count(f):
            f = i
    ind = labels0.count(f)
    if ind == 1:
        d0.roll_north()
    elif ind == 4:
        d0.roll_south()
    else:
        while d0.get_faces()[0] != f:
            d.roll_east()
    labels0 = d0.get_faces()
    

    ind0 = labels.index(labels0[0])
    ind1 = labels.index(labels0[1])
    if ind0 == 1:
        d.roll_north()
    elif ind0 == 4:
        d.roll_south()
    else:
        while d.get_faces()[0] != labels0[0]:
            d.roll_east()
    while d.get_faces()[1] != labels0[1]:
        d.roll_east()
        d.roll_south()
        d.roll_west()
    for i in range(2,6):
        if d.get_faces()[i] != labels0[i]:
            print('No')
            return
    print('Yes')
    return
            
main()
