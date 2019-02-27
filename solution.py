import copy
import numpy as np

#Inputs
matrix_1 = np.array([[2, 2, 2], [2, 2, 2], [2, 2, 2]])
matrix_2 = np.array([[2, 2, 2, 2,], [2, 1, 2, 1], [2, 2, 2, 1]])
matrix_3 = np.array([[3, 3, 3, 3, 3, 3], [3, 1, 2, 3, 1, 3], [3, 1, 2, 3, 1, 3], [3, 3, 3, 1, 3, 3]])
matrix_4 = np.array([[3, 3, 3, 3, 5, 3], [3, 0, 2, 3, 1, 3], [3, 1, 2, 3, 1, 3], [3, 3, 3, 1, 3, 3]])
matrix_5 = np.array([[5, 5, 5, 5, 5], [9, 1, 1, 1, 5], [5, 1, 5, 1, 5], [5, 1, 1, 1, 5], [5, 5, 5, 5, 5]])

inputs = np.array([matrix_1, matrix_2, matrix_3, matrix_4, matrix_5])

#Program Starts
def check_safe(i, j):
    return(i>=0 and j>=0 and i<n_rows and j<n_cols)

def fill_block(i, j, matrix):
    flow_x = [-1, 0, 0, 1]
    flow_y = [0, 1, -1, 0]
    
    init_h = matrix[i][j]
    fill = [[False for j in range(n_cols)] for i in range(n_rows)]
    fill_block_util(i, j, matrix, fill)
    
    for i in range(n_rows):
        for j in range(n_cols):
            if fill[i][j] == True:
                for k in range(4):
                    if matrix[i+flow_x[k]][j+flow_y[k]] == 0 or (matrix[i+flow_x[k]][j+flow_y[k]] <= init_h and fill[i+flow_x[k]][j+flow_y[k]] == False):
                        fill = [[False for j in range(n_cols)] for i in range(n_rows)]
                        return fill
    return fill
    

def fill_block_util(i, j, matrix, fill):
    if matrix[i][j] == 0:
        return
    while(1):
        for k in range(4):
            if (check_safe(i+flow_x[k], j+flow_y[k]) == False):
                return
            
            if (matrix[i+flow_x[k]][j+flow_y[k]] < matrix[i][j]):
                return
            
            if fill[i][j] == True:
                return
                
        fill[i][j] = True
        for k in range(4):
            fill_block_util(i+flow_x[k], j+flow_y[k], matrix, fill)
            
def water_fill(matrix):
    global blocks_filled
    for i in range(n_rows):
        for j in range(n_cols):
            if matrix[i][j] < max_height:
                to_fill = fill_block(i, j, matrix)
                for x in range(n_rows):
                    for y in range(n_cols):
                        if to_fill[x][y]:
                            blocks_filled += 1
                            matrix[x][y] += 1
                            
def WaterStoredInPlatform(platform):
    while(1):
        platform_init = copy.deepcopy(platform)
        water_fill(platform)
        if (platform == platform_init).all():
            return blocks_filled
        
for platform in inputs:
    n_rows = len(platform)
    n_cols = len(platform[0])

    max_height = -10e5
    for i in platform:
        temp = max(i)
        if temp > max_height:
            max_height = temp
    blocks_filled = 0
    
    print(WaterStoredInPlatform(platform))