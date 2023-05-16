def bubble_sort(list):
    n=len(list)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if list[j] > list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
                print("{} Iteration {}".format(list, i))


n=int(input("Enter the number of elements in linear array: "))
Array=list(map(int, input("enter elements: ").split()[:n]))
print("The array you entered: ",Array)
bubble_sort(Array)
print("Sorted: ",Array)