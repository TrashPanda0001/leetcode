
possible_options = [1,2,3]

def get_possible_paths_bottom_up(floor):
    if floor<0:
        return []
    elif floor==0:
        return [""]
    new_paths =[]
    for move in possible_options:
        paths = get_possible_paths_bottom_up(floor-move)
        for path in paths:
            new_paths.append(str(move)+path)
    return new_paths

def get_possible_paths_top_down(floor,auxilary_string,paths):
    if floor<0:
        return
    elif floor==0:
        paths.append(auxilary_string)
        return
    for move in possible_options:
        get_possible_paths_top_down(floor-move,auxilary_string+str(move),paths)


def get_stairs_path(floor):
    print(get_possible_paths_bottom_up(floor))
    paths =[]
    get_possible_paths_top_down(floor,"",paths)
    print(paths)


floor = input("enter floor")
get_stairs_path(int(floor))

#time complexity = len(possible_options)^n -> 3^n