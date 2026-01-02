class _Dice:
    
    def __init__(self, nums):
        self.nums = list(nums)
        
    @property
    def top(self):
        return self.nums[0]
        
    def _shift(self, *pairs):
        for pair in pairs:
            num = self.nums[pair[0]]
            self.nums[pair[0]] = self.nums[pair[1]]
            self.nums[pair[1]] = num
            
    def get_matches(self, num):
        return [i for i, m in enumerate(self.nums) if m == num]
            
    def go(self, opes:str):
        for ope in opes:
            if ope == "N":
                self.go_north()
            elif ope == "E":
                self.go_east()
            elif ope == "W":
                self.go_west()
            else:
                self.go_south()
                
    def go_top(self, index):
        
        if index == 1:
            self.go_north()
        elif index == 2:
            self.go_west()
        elif index == 3:
            self.go_east()
        elif index == 4:
            self.go_south()
        elif index == 5:
            self.go_north()
            self.go_north()
            
    def go_ahead(self, index):

        if index == 2:
            self.go_cw()
        elif index == 4:
            self.go_cw()
            self.go_cw()
        elif index == 3:
            self.go_ccw()
            
        
    def go_north(self):
        self._shift((0, 1), (1, 5), (5, 4))
        
    def go_east(self):
        self._shift((0, 3), (3, 5), (5, 2))
        
    def go_west(self):
        self._shift((0, 2), (2, 5), (5, 3))
        
    def go_south(self):
        self._shift((0, 4), (4, 5), (5, 1))
        
    def go_ccw(self):
        self._shift((3, 4), (4, 2), (2, 1))
        
    def go_cw(self):
        self._shift((3, 1), (1, 2), (2, 4))
        
        
class Dice(_Dice):
    
    @classmethod
    def isequal(cls, a:_Dice, b:_Dice):
                
        a_clone = a.nums.copy()
        for top in a.get_matches(b.nums[0]):
            a.go_top(top)
            a_top_clone = a.nums.copy()
            for ahead in a.get_matches(b.nums[1]):
                a.go_ahead(ahead)
                
                for i, j in zip(a.nums, b.nums):
                    if i != j:
                        break
                else:
                    return True
                
                a.nums = a_top_clone.copy()
                
            a.nums = a_clone.copy()
            
        else:
            return False
        
def check(dices):
    for i, dice_A in enumerate(dices):
        if i == len(dices) - 1:
            break
        
        for dice_B in dices[i + 1:]:
            if Dice.isequal(dice_A, dice_B):
                return False
        
    return True
        

count = int(input())
dices = [Dice(map(int, input().split())) for _ in range(count)]
print("Yes" if check(dices) else "No")
