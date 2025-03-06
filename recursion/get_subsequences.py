
def get_subsequences_bottom_up_approach(s,index):
    if(index==len(s)):
        return [""]
    subsequenceSoFar = get_subsequences_bottom_up_approach(s,index+1)
    new_subsequence = []
    for subsequence in subsequenceSoFar:
        new_subsequence.append(s[index] + subsequence)
        new_subsequence.append(subsequence)
    return new_subsequence


def get_subsequneces_top_down(s,index,auxilary_string,subsequences):
    if(index ==len(s)):
        subsequences.append(auxilary_string)
        return
    get_subsequneces_top_down(s,index+1,auxilary_string+s[index],subsequences)
    get_subsequneces_top_down(s,index+1,auxilary_string,subsequences)



s = input("Please enter a string")
print(get_subsequences_bottom_up_approach(s,0))
subsequences = []
get_subsequneces_top_down(s,0,"",subsequences)
print(subsequences)