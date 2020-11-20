class Solver:

    def __init__(self, table):
        self.table = table

    def start(self):
        self.solve(self.table)
    
    #assignes the location of the empty space coordinates in the grid to l, if there is no empty location return false (which indicates that we are done!)
    def findEmptySpace(self, mat,l):
        for i in range(9):
            for j in range(9):
                if mat[i][j] == 0:
                    l[0] = i
                    l[1] = j
                    return True
        return False

    #Checks if the move is legal
    def isLegal(self, mat,row,col,num):
        return not self.inRow(mat,row,num) and not self.inBox(mat,row - row %3,col - col %3,num) and not self.inCol(mat,col,num)


    #Checks if the number is in the row, true if there is such a number
    def inRow(self, mat,row,num):
        for col in range(9):
            if mat[row][col] == num:
                return True
        return False

    #Checks if the number is in the coloumn
    def inCol(self,mat,col,num):
        for row in range(9):
            if mat[row][col] == num:
                return True
        return False

    #Checks if the number is in the box
    def inBox(self,mat,row,col,num):
        for i in range(3):
            for j in range(3):
                if mat[row + i][col + j] == num:
                    return True
        return False

    #prints the table 
    def printGrid(self, mat):
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                print (mat[i][j], end = ' ')
            print ()


    def solve(self,sudokuTable):
        l = [0,0] #Empty space coordinates

        #If there is no unassigned space, the sudoku is solved
        if not self.findEmptySpace(sudokuTable,l):
            return True
        row = l[0]
        col = l[1]

        #Starting number assignment
        for num in range(1,10):
            if self.isLegal(sudokuTable,row,col,num):
                sudokuTable[row][col] = num
                if self.solve(sudokuTable):
                    return True
                sudokuTable[row][col] = 0

        return False




if __name__=="__main__":
    sudoku =[
            [3, 0, 6, 5, 0, 8, 4, 0, 0], 
            [5, 2, 0, 0, 0, 0, 0, 0, 0], 
            [0, 8, 7, 0, 0, 0, 0, 3, 1], 
            [0, 0, 3, 0, 1, 0, 0, 8, 0], 
            [9, 0, 0, 8, 6, 3, 0, 0, 5], 
            [0, 5, 0, 0, 9, 0, 6, 0, 0], 
            [1, 3, 0, 0, 0, 0, 2, 5, 0], 
            [0, 0, 0, 0, 0, 0, 0, 7, 4], 
            [0, 0, 5, 2, 0, 6, 3, 0, 0]] 

    solution = Solver(sudoku)
    solution.start()
    solution.printGrid(sudoku)
