"""
# Intuition
We need to effectively check if 27 arrays are valid, since we need to check all rows, all columns, and all boxes (there are mathematical proofs out there that say that we don't need to check all 27 arrays, but for simplicity I decided to check all 27)

# Approach
For rows:
We only need to use one array, as for every iteration of the inner loop, we iterate through an entire row. Thus, we can store the values of a given row to the array row. At the end of one iteration of the inner loop, provided the row is valid, we can then erase the array row and use it for the next row.

For columns:
In contrast, we need to use nine arrays for the columns. Once we approach the ninth row, we can then check if the columns are valid.

For boxes:
We only need to use three rows, as when we reach the end of the 3rd, 6th, and 9th rows, we can then check the three boxes and determine if they are valid.

To determine if an array is valid:
I sort the array, which means duplicate values that exist would be next to each other. If there are duplicate values in the array, return False.

# Complexity
- Time complexity:
Sorting arrays to find duplicates: O(n log n)
Since the rest of the operations happen in linear time, this dominates.

- Space complexity:
Creating 27 lists of length 9: O(27*9) -> O(n)
"""

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
                
            # Reached end of row, check row
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

            if j == 8: # Reached end of column, check columns
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
