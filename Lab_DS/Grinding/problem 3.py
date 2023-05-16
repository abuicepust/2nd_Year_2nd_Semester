def linear_src(mylist, element):
    for pos in range(len(mylist)):
        if mylist[pos]== element:
            return pos
    return -1


n=int(input("Enter the number of elements: "))
array=list(map(int, input("Enter the elements: ").split()[:n]))
print("The array you entered: ",array)
num=int(input("Enter search element: "))
position=linear_src(array,num)
if position== -1:
    print("Not found")
else:
    print("Found at",position+1)
