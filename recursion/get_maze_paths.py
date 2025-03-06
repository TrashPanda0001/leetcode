def get_maze_path_combinations_bottom_up(rows, columns,cur_row,cur_column):
    if cur_row>=rows or cur_column>=columns:
        return []
    elif cur_row==rows-1 and cur_column==columns-1:
        return [""]
    paths = []
    down_paths = get_maze_path_combinations_bottom_up(rows,columns,cur_row+1,cur_column)
    right_paths = get_maze_path_combinations_bottom_up(rows,columns,cur_row,cur_column+1)
    for path in down_paths:
        paths.append("v"+path)
    for path in right_paths:
        paths.append("h"+path)
    return paths


def get_maze_path_combinations_top_down(rows, columns,cur_row,cur_column,auxilary_string,paths):
    if cur_row>=rows or cur_column>=columns:
        return
    elif cur_row==rows-1 and cur_column==columns-1:
        paths.append(auxilary_string)
        return
    down_paths = get_maze_path_combinations_top_down(rows,columns,cur_row+1,cur_column,auxilary_string+"v",paths)
    right_paths = get_maze_path_combinations_top_down(rows,columns,cur_row,cur_column+1,auxilary_string+"h",paths)


def get_maze_paths(rows,columns):
    print(get_maze_path_combinations_bottom_up(rows,columns,0,0))
    paths = []
    get_maze_path_combinations_top_down(rows,columns,0,0,"",paths)
    print(paths)


rows = input("enter number of rows")
columns = input("enter number of columns")
get_maze_paths(int(rows),int(columns))

#time complexity -> 2^n
# similar leetcode question -> https://leetcode.com/problems/unique-paths/description/