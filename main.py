from ai import MinMax
algorithm = MinMax()

class process:
    def pass_input(self,cell):
        board , check = algorithm.current_table()
        result = algorithm.evaluate(board ,check)
        if result == 'X' or result == 'O' or result == 'D': 
            result=[]
            for i in range(3):
                for j in range(3):
                    result.append(board[i][j])
            return result
        if 1 <= cell <= 9:
            r, c = (cell - 1) // 3, (cell - 1) % 3
            board = algorithm.User(r,c)
            if board:
                result=[]
                for i in range(3):
                    for j in range(3):
                        result.append(board[i][j])
                return result
    def restart(self):
        return algorithm.restart()

    def status(self):
        board , check = algorithm.current_table()
        result = algorithm.evaluate(board ,check)
        if result == 'X':
            return "You Lose 💀"
        elif result == 'O':
            return " You Won 🤯"
        elif result == "D":
            return "Drawn 🕊️"
        return "Ongoing ⚔️"