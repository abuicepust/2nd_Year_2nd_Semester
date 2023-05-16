n=int(input("Enter the number of elements"))
Array=list(map(int, input("Enter array Numbers").split()[:n]))
print("Arrays you entered",Array)
while 1:
    print("n\Options\n1.Insert\n2.Delete\n3.Exit")
    str=int(input("Type 1 2 or 3\n"))
    if (str==1):
        print("Before Inserted The array",Array)
        pos=int(input("Enter the position of the element"))
        num=int(input("Enter the number"))
        Array.insert(pos,num)
        print("After Insertion",Array)
    elif(str==2):
        print("Before Deleted The array", Array)
        num = int(input("Enter the number"))
        Array.remove(num)
        print("After Deletion", Array)
    else:
        print("Exit")
