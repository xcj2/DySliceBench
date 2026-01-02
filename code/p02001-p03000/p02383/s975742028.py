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
        
def main():
    labels = list(map(int, input().split()))
    orders = input()
    d = Dice(labels)
    for o in orders:
        if o == 'S':
            d.roll_south()
        elif o == 'E':
            d.roll_east()
        elif o == 'W':
            d.roll_west()
        elif o == 'N':
            d.roll_north()
    print(d)
    
main()
