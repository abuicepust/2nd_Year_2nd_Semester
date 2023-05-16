# Department of ICE, Pabna University of Science and Technology
# Name: Md. Abu Yousuf
# Roll: 180640
# Session: 2017-2018
# Course Code: ICE-2202
# Course Title: Data Structure and Algorithm Sessional

def merge_Sort(MyList):
    if len(MyList) > 1:
        mid = len(MyList) // 2
        left = MyList[:mid]
        right = MyList[mid:]

        merge_Sort(left) #divide two parts
        merge_Sort(right)
        i=j=k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                # The value from the left half has been used
                MyList[k] = left[i]
                i += 1
            else:
                MyList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1
        # For all the remaining values
        while i < len(left):
            MyList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            MyList[k] = right[j]
            j += 1
            k += 1
#function from fully ascending order array.
#function close
n = int(input("Enter number of elements in linear array : "))
Array=list(map(int, input("Enter array elements : ").split()[:n]))
print("Before not using merge_Sort then linear array : ",Array)
merge_Sort(Array)
print("After using merge_Sort then linear array : ",Array)