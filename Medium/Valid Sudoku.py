class Solution(object):
    def has_duplicates(self, arr):
        arr.sort()
        length = len(arr)
        i = 1
        while i < length:
            if arr[i] == arr[i-1] and arr[i] != '.':
                return False
            else:
                i += 1
        
        return True

    def isValidSudoku(self, board):
        """
        We need to check if 27 arrays of length 9 are all valid (we check if an array is valid by sorting and determining if there are duplicates)
        To check all rows, we can simply use one array, since the nested for loop iterates through one row and we can update the array at the end of the inner loop
        To check all boxes, we can use three arrays, as the boxes will get filled at the end of the 3rd, 6th, and 9th rows
        To check all columns, we need to have nine arrays, as we need to store that information until we reach the 9th row and then we can check if a column is valid
        """
        row = []
        col1 = []
        col2 = []
        col3 = []
        col4 = []
        col5 = []
        col6 = []
        col7 = []
        col8 = []
        col9 = []
        box1 = []
        box2 = []
        box3 = []
        rows = len(board)
        cols = len(board[0])

        for j in range(cols):
            for i in range(rows):
                row.append(board[i][j])
                if i == 0:
                    col1.append(board[i][j])
                if i == 1:
                    col2.append(board[i][j])
                if i == 2:
                    col3.append(board[i][j])
                if i == 3:
                    col4.append(board[i][j])
                if i == 4:
                    col5.append(board[i][j])
                if i == 5:
                    col6.append(board[i][j])
                if i == 6:
                    col7.append(board[i][j])
                if i == 7:
                    col8.append(board[i][j])
                if i == 8:
                    col9.append(board[i][j])
                if i < 3:
                    box1.append(board[i][j])
                if i < 6 and i >= 3:
                    box2.append(board[i][j])
                if i < 9 and i >= 6:
                    box3.append(board[i][j])
                
            # Reached end of row, check rowSum
            if not self.has_duplicates(row):
                return False
            row = []

            if (j + 1) % 3 == 0 and j != 0:# Created 3 boxes, check boxes
                if not self.has_duplicates(box1):
                    return False
                box1 = []
                if not self.has_duplicates(box2):
                    return False
                box2 = []
                if not self.has_duplicates(box3):
                    return False
                box3 = []

            if j == 8: # Reached end of column, check colSum
                if not self.has_duplicates(col1):
                    return False
                col1 = []
                if not self.has_duplicates(col2):
                    return False
                col2 = []
                if not self.has_duplicates(col3):
                    return False
                col3 = []
                if not self.has_duplicates(col4):
                    return False
                col4 = []
                if not self.has_duplicates(col5):
                    return False
                col5 = []
                if not self.has_duplicates(col6):
                    return False
                col6 = []
                if not self.has_duplicates(col7):
                    return False
                col7 = []
                if not self.has_duplicates(col8):
                    return False
                col8 = []
                if not self.has_duplicates(col9):
                    return False
                col9 = []

            
        
        return True
        """
        :type board: List[List[str]]
        :rtype: bool
        """
