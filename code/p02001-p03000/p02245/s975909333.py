from collections import deque

class Puzzle:
    def __init__(self, ls, answer_flag=False):
        self.piece_vec = list(ls)
        self.update_value = [-3, 3, -1, 1]
        for idx, piece in enumerate(ls):
            if piece == 0:
                self.space_idx = idx
        
        self.space_idx_before_slide = deque()
        self.manhattan_distance = list()
        if answer_flag:
            for i in range(9):
                self.manhattan_distance.append([(abs(i % 3 - j % 3) + abs(i // 3 - j // 3)) for j in range(9)])
                    
        
    def GetManhattanDistance(self, ans_idx, idx):
        return self.manhattan_distance[ans_idx][idx]
        
    def SumManhattanDistance(self, answer_board):
        sum_MD = 0
        for idx, piece in enumerate(self.piece_vec):
            if piece == 0:
                continue
            answer_idx = piece - 1
            sum_MD += answer_board.GetManhattanDistance(answer_idx, idx)
        return sum_MD
    
    def SlideSpace(self, command):
        is_frame = [self.space_idx < 3, self.space_idx >= 6, self.space_idx % 3 == 0, self.space_idx % 3 == 2]
        if is_frame[command]:
            return False
        
        next_space_idx = self.space_idx + self.update_value[command]
        if len(self.space_idx_before_slide) > 0 and next_space_idx == self.space_idx_before_slide[-1]:
            return False
        
        self.piece_vec[self.space_idx], self.piece_vec[next_space_idx] = self.piece_vec[next_space_idx], self.piece_vec[self.space_idx]
        self.space_idx_before_slide.append(self.space_idx)
        self.space_idx = next_space_idx
        return True
    
    def BackState(self):
        self.piece_vec[self.space_idx], self.piece_vec[self.space_idx_before_slide[-1]] = self.piece_vec[self.space_idx_before_slide[-1]], self.piece_vec[self.space_idx]
        self.space_idx = self.space_idx_before_slide.pop()

def SolvePuzzleByDFS(board, answer_board, limit, depth = 0):
    if board.SumManhattanDistance(answer_board) == 0:
        return True
    
    if depth + board.SumManhattanDistance(answer_board) > limit:
        return False
    
    for command in range(4):
        if board.SlideSpace(command) == False:
            continue
        
        if SolvePuzzleByDFS(board, answer_board, limit, depth+1):
            return True
        board.BackState()
    
    return False

def CalcMinStepOf15Puzzle(board, answer_board):
    for limit in range(board.SumManhattanDistance(answer_board), 35):
        if SolvePuzzleByDFS(board, answer_board, limit):
            return limit
    
    return -1

def main():
    inputLs = list()
    answerLs = [ 1, 2, 3,
                 4, 5, 6, 
                 7, 8, 9]
    for _ in range(3):
        inputLs += list(map(int, input().split()))

    start_board = Puzzle(inputLs)
    answer_board = Puzzle(answerLs, True)
    
    min_step = CalcMinStepOf15Puzzle(start_board, answer_board);
    
    print(min_step)

if __name__ == '__main__':
    main()

