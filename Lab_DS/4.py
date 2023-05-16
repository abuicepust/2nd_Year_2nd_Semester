# Department of ICE, Pabna University of Science and Technology
# Name: Md. Abu Yousuf
# Roll: 180640
# Session: 2017-2018
# Course Code: ICE-2202
# Course Title: Data Structure and Algorithm Sessional

def binary_search(MyList,element,start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if element == MyList[mid]:
        return mid
    if element < MyList[mid]:
        return binary_search(MyList, element, start, mid-1)#using recursive function
    else:
        return binary_search(MyList, element, mid+1, end)

 #function close
n = int(input("Enter number of elements in linear array : "))
Array=list(map(int, input("Enter array numbers : ").split()[:n]))
print("All linear array element is : ",Array)
num=int(input("Enter search element : "))
position = binary_search(Array,num,0,len(Array)-1)
if position == -1:
    print("Element is not present in this array ")
else :
    print("Use binary_search algorithm element present position is :",position+1)