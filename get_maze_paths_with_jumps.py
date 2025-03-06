



def getPaths(rows,columns,cur_row,cur_col):
    if(cur_row>=rows or cur_col>=columns):
        return []
    elif cur_col==columns-1 and cur_row==rows-1:
        return [""]
    new_paths = []
    for i in range(1,rows-cur_row+1):
        paths = getPaths(rows,columns,cur_row+i,cur_col)
        for path in paths:
            new_paths.append(f"v{i}"+path)
    for i in range(1,columns-cur_col+1):
        paths = getPaths(rows,columns,cur_row,cur_col+i)
        for path in paths:
            new_paths.append(f"h{i}"+path)
    for i in range(1,min(rows-cur_row+1,columns-cur_col+1)):
        paths = getPaths(rows,columns,cur_row+i,cur_col+i)
        for path in paths:
            new_paths.append(f"d{i}"+path)
    return new_paths






rows = int(input("enter rows"))
columns = int(input("enter columns"))
def get_maze_paths_with_jumps(rows,columns):
    print(getPaths(rows,columns,0,0))

get_maze_paths_with_jumps(rows, columns)