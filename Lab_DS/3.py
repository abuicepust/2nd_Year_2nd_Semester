# Department of ICE, Pabna University of Science and Technology
# Name: Md. Abu Yousuf
# Roll: 180640
# Session: 2017-2018
# Course Code: ICE-2202
# Course Title: Data Structure and Algorithm Sessional

def linear_search(MyList,element):
    for pos in range(len(MyList)):
        if MyList[pos] == element:
            return pos
    return -1
#function close
n = int(input("Enter the number of elements in linear array : "))
Array=list(map(int, input("Enter array numbers : ").split()[:n]))
print("All linear array element is : ",Array)
num=int(input("Enter search element : "))
position = linear_search(Array,num)
if position == -1:
    print("Element is not present in this array ")
else :
    print("Use linear_search algorithm element present position is :",position+1)