# Department of ICE, Pabna University of Science and Technology
# Name: Md. Abu Yousuf
# Roll: 180640
# Session: 2017-2018
# Course Code: ICE-2202
# Course Title: Data Structure and Algorithm Sessional

def bubblesrt(MyList):
    n = len(MyList)    #Logic
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if MyList[j] > MyList[j + 1]:
                MyList[j], MyList[j + 1] = MyList[j + 1], MyList[j] #swaping two elements
#End of the function
n = int(input("How many elements in the linear array : "))
Array=list(map(int, input("Enter array numbers : ").split()[:n]))
print("All linear array element is : ",Array)
print("Before using algorithm the linear array : ",Array)
bubblesrt(Array)
print("After using algorithm the linear array : ",Array)








