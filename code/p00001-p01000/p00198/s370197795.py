class Dice:
    same_dice_index = ((0, 1, 2, 3, 4, 5), (0, 2, 4, 1, 3, 5), (0, 3, 1, 4, 2, 5),
                       (0, 4, 3, 2, 1, 5), (1, 0, 3, 2, 5, 4), (1, 2, 0, 5, 3, 4),
                       (1, 3, 5, 0, 2, 4), (1, 5, 2, 3, 0, 4), (2, 0, 1, 4, 5, 3),
                       (2, 1, 5, 0, 4, 3), (2, 4, 0, 5, 1, 3), (2, 5, 4, 1, 0, 3),
                       (3, 0, 4, 1, 5, 2), (3, 1, 0, 5, 4, 2), (3, 4, 5, 0, 1, 2),
                       (3, 5, 1, 4, 0, 2), (4, 0, 2, 3, 5, 1), (4, 2, 5, 0, 3, 1),
                       (4, 3, 0, 5, 2, 1), (4, 5, 3, 2, 0, 1), (5, 1, 3, 2, 4, 0),
                       (5, 2, 1, 4, 3, 0), (5, 3, 4, 1, 2, 0), (5, 4, 2, 3, 1, 0))

    def __init__(self, str_list):
        self.faces = str_list

    def is_same(self, dice):
        for i in Dice.same_dice_index:
            for n, j in enumerate(i):
                if dice.faces[n] != self.faces[j]:
                    break
            else:
                return True
        return False

    def is_unique(self, dices_list):
        for i in dices_list:
            if self.is_same(i):
                return False
        return True

def solve():
    from sys import stdin
    f_i = stdin
    
    ans_list = []
    
    while True:
        n = int(f_i.readline())
        
        if n == 0:
            break
        
        dices = [Dice(f_i.readline().split()) for i in range(n)]
        
        ans = 0
        while dices:
            tmp_dices = []
            d1 = dices.pop()
            for d2 in dices:
                if d1.is_same(d2):
                    ans += 1
                else:
                    tmp_dices.append(d2)
            dices = tmp_dices
        
        ans_list.append(ans)
    
    print('\n'.join(map(str, ans_list)))

solve()
