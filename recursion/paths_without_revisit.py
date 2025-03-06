moves =[(1,0,"D"),(0,1,"R"),(-1,0,"U"),(0,-1,"L")]
def getPaths(arr,rows,columns,cur_row,cur_column):
    if cur_row<0 or cur_column<0 or cur_row>=rows or cur_column>=columns or arr[cur_row][cur_column]==-1:
        return []
    elif cur_row==rows-1 and cur_column==columns-1:
        return [""]
    new_paths = []
    for move in moves:
        x_move = move[0]
        y_move=move[1]
        move_sign = move[2]
        temp_value = arr[cur_row][cur_column]
        arr[cur_row][cur_column]=-1
        paths = getPaths(arr,rows,columns,cur_row+x_move,cur_column+y_move)
        for path in paths:
            new_paths.append(move_sign+path)
        arr[cur_row][cur_column]=temp_value
    return new_paths


rows = int(input("enter number of rows"))
columns = int(input("enter number of columns"))
arr = [[0] * columns for i in range(rows)]
print(getPaths(arr,rows,columns,0,0))



