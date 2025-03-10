
















def getPairings(n,k,subsets,sets_so_far,num):
    if num>n:
        if sets_so_far==k:
            print(subsets)
        return
    for i in range(k):
        if len(subsets[i]) ==0:
            subsets[i].append(num)
            getPairings(n,k,subsets,sets_so_far+1,num+1)
            subsets[i].remove(num)
        else:
            subsets[i].append(num)
            getPairings(n,k,subsets, sets_so_far,num+1)
            subsets[i].remove(num)
            break #->https://youtu.be/TvvGj1FtHIk?t=549 -> only choose the first empty as it is the same thing






n = int(input("Enter number n"))
k = int(input("Enter number k"))
subsets = [[] for _ in range(k)]
getPairings(n,k,subsets,0,1)