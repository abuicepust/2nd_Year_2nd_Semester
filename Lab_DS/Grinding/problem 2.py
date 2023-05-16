
def bubblesrt(mylist):
    n=len(mylist)
    for i in range(n - 1):
        for j in range(0, n-i-1):
            if mylist[j] > mylist[j+1]:
                mylist[j],mylist[j+1]=mylist[j+1],mylist[j]
                print(mylist)

n=int(input("Enter How many element in array: "))
array=list(map(int, input("Enter the arrays: ").split()[:n]))
print("arrays you entered: ",array)
bubblesrt(array)
print(array)



