numbers=[]
def getNumbers(n,num):
    if num>n:
        return
    numbers.append(num)
    for i in range(0,10):
        getNumbers(n,num*10+i)

n = int(input("enter a number"))
for i in range(1,10):
    getNumbers(n,i)
print(numbers)