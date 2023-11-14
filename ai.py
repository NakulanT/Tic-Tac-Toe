from collections import defaultdict
import random

class MinMax:
    def __init__(self) -> None:
        self.table = [["","",""] ,["","",""],["","",""]]
        self.count = defaultdict(int)
        for r in range(3):
            for c in range(3):
                if self.table[r][c] != "" :
                    self.count[self.table[r][c]] += 1
                    
                    
    def User(self,r,c):
        if self.table[r][c] == "":
            self.table[r][c] = "O"
            self.count["O"] += 1 
            self.play()
            return self.table
        return None
            
    def display(self):
        print("")
        print("-------------")
        for i in self.table:
            print("¦ ", end="")
            for j in i:
                print(j, end=" ¦ ")
            print("")
            print("-------------")
        print("")


    def checkmate(self):
        result = self.evaluate(self.table,self.count)
        if not result:
            return False
        return result

    def play(self):
        if self.checkmate():
            return 
        bestscore = float('-inf')
        bestpositions = []
        for r in range(3):
            for c in range(3):
                if self.table[r][c] == "":
                    self.table[r][c] = 'X'
                    self.count['X'] += 1
                    score = self.minmax(self.table, self.count,10, False)
                    self.table[r][c] = ""
                    self.count['X'] -= 1
                    if score > bestscore:
                        bestscore = score
                        bestpositions = [[r, c]]
                    elif score == bestscore:
                        bestpositions.append([r, c])
        if bestpositions:
            bestposition = random.choice(bestpositions)
            self.table[bestposition[0]][bestposition[1]] = "X"
            self.count["X"] += 1
            return self.table
        else:
            print("ERROR")

    def minmax(self, board,count,depth, is_maximizing):
        result = self.checkmate()
        if result == 'X':
            return 1 
        elif result == 'O':
            return -1
        elif result == 'D':
            return 0

        if is_maximizing:
            value = float('-inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "":
                        board[i][j] = "X"
                        count["x"] += 1
                        score = self.minmax(board, count ,depth - 1, False)
                        board[i][j] = ""
                        count["x"] -= 1
                        value = max(value, score)
            return value
        else:
            value = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "":
                        board[i][j] = "O"
                        count["O"] += 1
                        score = self.minmax(board, count ,depth - 1, True)
                        board[i][j] = ""
                        count["O"] -= 1
                        value = min(value, score)
            return value


    def evaluate(self , board , count):
        check = {'R1': set(), 'R2': set(), 'R3': set(),
                 'C1': set(), 'C2': set(), 'C3': set(),
                 'PD': set(), 'ND': set(), }
        
        for r in range(3):
            for c in range(3):
                # rows
                if r == 0:
                    check['R1'].add(board[r][c])
                elif r == 1:
                    check['R2'].add(board[r][c])
                elif r == 2:
                    check['R3'].add(board[r][c])
                # cols
                if c == 0:
                    check['C1'].add(board[r][c])
                elif c == 1:
                    check['C2'].add(board[r][c])
                elif c == 2:
                    check['C3'].add(board[r][c])
                # Diagonal
                if r - c == 0:
                    check['PD'].add(board[r][c])
                if r + c == 2:
                    check['ND'].add(board[r][c])

        # Prioritize blocking the opponent
        for i in check:
            if 'O' in check[i] and len(check[i]) == 1 and 'X' not in check[i]:
                return 'O'

        # Check if AI wins
        for i in check:
            if 'X' in check[i] and len(check[i]) == 1 and 'O' not in check[i]:
                return 'X'  # AI wins

        if sum(count.values()) == 9:
            return 'D'  # Draw

        return None

    def restart(self):
        self.table = [["","",""] ,["","",""],["","",""]]
        self.count = defaultdict(int)
        for r in range(3):
            for c in range(3):
                if self.table[r][c] != "" :
                    self.count[self.table[r][c]] += 1 
        return [""]*9
    
    
    def current_table(self):
        return(self.table , self.count)