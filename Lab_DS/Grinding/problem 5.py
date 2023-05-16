def merge_sort(mylist):
    if len(mylist)>1:
        mid=len(mylist)//2
        left=mylist[:mid]
        right=mylist[mid:]
        merge_sort(left)
        merge_sort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                mylist[k]=left[i]
                i += 1
            else:
                mylist[k]=right[j]
                j += 1
            k += 1
        while i<len(left):
            mylist[k]=left[i]
            i += 1
            k += 1
        while j<len(right):
            mylist[k]=right[j]
            j += 1
            k += 1



n=int(input("Enter the number of elements: "))
array=list(map(int, input("Enter the elements: ").split()[:n]))
print("Arrays you entered: ",array)
merge_sort(array)
print("Sorted arry",array)
