class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        captured_idx = []
        row_idx = []
        # get the index number for the row with element as 0
        for i in range(len(matrix)):
            print(matrix[i])
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    # capture the index
                    captured_idx.append(j)
                    # capture the row index
                    row_idx.append(i)
            
        print(captured_idx, row_idx)
                    
        # setting all the values for the given row as 0
        for r_idx in row_idx:
            for k in range(len(matrix[r_idx])):
                matrix[r_idx][k] = 0
                
        # setting all the values for tbhe given column to be 0
        for col_idx in captured_idx:
            for l in range(len(matrix)):
                matrix[l][col_idx] = 0
            
        
        