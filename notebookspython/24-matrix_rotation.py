def rotate(matrix):
    n = len(matrix)
    
    # 1. 转置矩阵：只遍历对角线以上的部分，避免重复交换
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    # 2. 反转每一行
    for i in range(n):
        matrix[i].reverse()