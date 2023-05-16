def Linear_search(list,element):
    n=len(list)
    for pos in range(n):
        if list[pos]==element:
            return pos
    return -1





n=int(input("Enter how many element in LA: "))
Array=list(map(int, input("Enter the elements: ").split()[:n]))
print("The Linear Array: ",Array)
num=int(input("Enter search Element: "))
position=Linear_search(Array,num)
if position==-1:
    print("Not found")
else:
    print("Found at",position+1)