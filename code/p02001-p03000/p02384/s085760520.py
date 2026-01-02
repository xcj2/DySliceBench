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
    labels = list(map(int, input().split()))
    d = Dice(labels)
    n = int(input())
    for i in range(n):
        faces = list(map(int, input().split()))
        ind0 = labels.index(faces[0])
        ind1 = labels.index(faces[1])
        if ind0 == 1:
            d.roll_north()
        elif ind0 == 4:
            d.roll_south()
        else:
            while d.get_faces()[0] != faces[0]:
                d.roll_east()
        while d.get_faces()[1] != faces[1]:
            d.roll_east()
            d.roll_south()
            d.roll_west()
        print(d.get_faces()[2])
        
main()
