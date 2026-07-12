def setZeroes(matrix):
    if not matrix:
        return
    
    rows, cols = len(matrix), len(matrix[0])
    first_row_has_zero = any(matrix[0][j] == 0 for j in range(cols))
    first_col_has_zero = any(matrix[i][0] == 0 for i in range(rows))
    
    # 1. 使用第一行和第一列作为标记
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
                
    # 2. 根据标记清零内部矩阵
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
                
    # 3. 最后清零第一行和第一列
    if first_row_has_zero:
        for j in range(cols):
            matrix[0][j] = 0
            
    if first_col_has_zero:
        for i in range(rows):
            matrix[i][0] = 0