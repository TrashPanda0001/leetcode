


def getNumberOfWays(n,k):
    if n==k:
        return 1
    if k>n or k==0 or n==0:
        return 0
    if k==1:
        return 1
    return k*getNumberOfWays(n-1,k) + getNumberOfWays(n-1,k-1) #-> agar n-1 logo ne k sets already bana diye then nth person can go sit in any of the k sets , if n-1 logo ne k-1 set banaye then nth person has no choice but o make the kth set
n = int(input("enter n"))
k = int(input("enter k"))
print(str(getNumberOfWays(n,k)))