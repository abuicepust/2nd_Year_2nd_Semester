
n=int(input("Enter the number of elements: "))
Array=list(map(int, input("Enter the numbers: ").split()[:n]))
print("Number you entered: ",Array)
while 1:
    print("Enter what you want?\n1.Insert\n2.Delete\n3.Exit")
    str=int(input("\nEnter 1 2 or 3"))
    if str==1:
        print("Before Insertion: ",Array)
        pos = int(input("Enter the position: "))
        num=int(input("Enter the number to insert: "))
        Array.insert(pos,num)
        print("After insertion: ",Array)
    if(str==2):
        print("Before deleted the value: ",Array)
        num=int(input("Enter the deleted number: "))
        Array.remove(num)
        print("After deleted the numb: ",Array)
    else:
        exit()

