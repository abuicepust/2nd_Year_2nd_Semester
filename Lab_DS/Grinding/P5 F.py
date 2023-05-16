def Merge_sort(list):
    if len(list) > 1:
        mid=len(list)//2
        left = list[:mid]
        right = list[mid:]
        Merge_sort(left)
        Merge_sort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if(left[i]<=right[j]):
                list[k]=left[i]
                i += 1
            else:
                list[k]=right[j]
                j += 1
            k += 1
        while i<len(left):
            list[k]=left[i]
            i += 1
            k += 1
        while j<len(right):
            list[k]=right[j]
            j += 1
            k += 1




n=int(input("Enter the number of elements: "))
Array=list(map(int, input("Enter the elements; ").split()[:n]))
print("Before sorting Array: ",Array)
Merge_sort(Array)
print("Sorted Array",Array)