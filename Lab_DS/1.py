# Department of ICE, Pabna University of Science and Technology
# Name: Md. Abu Yousuf
# Roll: 180640
# Session: 2017-2018
# Course Code: ICE-2202
# Course Title: Data Structure and Algorithm Sessional

n = int(input("Enter number of elements in linear array : "))
#Using map() function
Array=list(map(int, input("Enter array numbers : ").split()[:n]))
print("Array's you entered : ",Array)
while 1:
    print("\nOptions\n1.Insert\n2.Delete\n3.Exit")
    str=int(input("Type 1 or 2 or 3\n"))
    if (str==1):
        print("Before insert the linear array : ",Array)
        pos = int(input("Enter insert position of array : "))
        num = int(input("Enter insert number : "))
        Array.insert(pos,num)
        print("The linear array now : ",Array)
    elif (str==2):
        print("Before delete element the linear array : ",Array)
        num = int(input("Enter delete number : "))
        Array.remove(num)
        print("The linear array now : ",Array)
    else :
        print("Exit")