from copy import deepcopy
from copy import copy

class Dice:
    def __init__(self, labels):
        self.surface = {x: labels[x-1] for x in range(1, 6+1)}
    def move_towards(self, direction):
        if direction == 'N':
            self._move(1, 2, 6, 5)
        elif direction == 'S':
            self._move(1, 5, 6, 2)
        elif direction == 'E':
            self._move(1, 4, 6, 3)
        elif direction == 'W':
            self._move(1, 3, 6, 4)
    def get_upper(self):
        return self.surface[1]
    def _move(self, i, j, k, l):
        temp_label = self.surface[i]
        self.surface[i] = self.surface[j]
        self.surface[j] = self.surface[k]
        self.surface[k] = self.surface[l]
        self.surface[l] = temp_label
    
    def find_pattern(self, pattern):
        dice = deepcopy(self)
        if dice.surface[1] == pattern[0] and dice.surface[2] == pattern[1]:
            return dice.surface[3]
        
        pattern_tested = {'original': dice.surface}
        moves = ['N', 'S', 'E', 'W']
        
        def find(dice, moves):
            next_moves = []
            for move in moves:
                if len(move) == 1:
                    start = 'original'
                else:
                    start = move[:-1]
                    
                dice.surface =pattern_tested[start]
                dice.move_towards(move[-1])
                
                if dice.surface[1] == pattern[0] and dice.surface[2] == pattern[1]:
                    right_label = dice.surface[3]
                    return right_label
                else:
                    move_tested = move
                    pattern_tested[move_tested] = copy(dice.surface)
                    next_moves.extend([move+'N', move+'S', move+'E', move+'W'])
            return find(dice, next_moves)
                
        return find(dice, moves)
    
labels = list(map(int, input().split()))
num_questions = int(input())
questions = [list(map(int, input().split())) for _ in range(num_questions)]
dice = Dice(labels)
results = []

for question in questions:
    right_label = dice.find_pattern(question)
    results.append(right_label)

for result in results:
    print(result)
