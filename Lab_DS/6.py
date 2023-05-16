# Department of ICE, Pabna University of Science and Technology
# Name: Md. Abu Yousuf
# Roll: 180640
# Session: 2017-2018
# Course Code: ICE-2202
# Course Title: Data Structure and Algorithm Sessional

def Selection_sort(MyList):
    for i in range(len(MyList) - 1):
        minimum = i
        for j in range( i + 1, len(MyList)):
            if(MyList[j] < MyList[minimum]):
                minimum = j
        if(minimum != i):
            MyList[i], MyList[minimum] = MyList[minimum], MyList[i]
    return MyList
#function close
n = int(input("Enter number of elements in linear array : "))
Array=list(map(int, input("Enter array elements : ").split()[:n]))
print("Before not using selection sort then linear array : ",Array)
Selection_sort(Array)
print("After using selection sort then linear array : ",Array)
