from audioop import reverse


def getFinalPermutations(s, extra,string_so_far):
    if len(s)==0:
        print(string_so_far + extra + string_so_far[::-1])
        return

    for i in range(0,len(s)):
        char = s[i]
        string_left = s[0:i] + s[i+1:]
        getFinalPermutations(string_left,extra, string_so_far+char)


def getPalindromicPermutations(s):
    freq_map ={}
    odd_count=0
    extra = ""
    string_to_permuate = ""
    for char in s :
        freq_map[char] = freq_map.get(char,0)+1
    for char in freq_map.keys():
        if freq_map.get(char)%2:
            odd_count+=1
            extra = char
        string_to_permuate+= char * (freq_map.get(char)//2)

    if odd_count>1:
        print("No palindromic permuatations")
        return
    return getFinalPermutations(string_to_permuate,extra,"")

s = input("Enter String")
getPalindromicPermutations(s)