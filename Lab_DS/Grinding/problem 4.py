def binary_src(mylist,element,start,end):
    if start>end:
        return -1
    mid=(start+end)//2
    if element==mylist[mid]:
        return mid
    if element<mylist[mid]:
        return binary_src(mylist,element,start,mid-1)
    if element>mylist[mid]:
        return binary_src(mylist,element,mid+1,end)



n=int(input("Enter the number of elements: "))
array=list(map(int, input("Enter elements: ").split()[:n]))
print("The elememnts",array)
num=int(input("Enter the search element: "))
position= binary_src(array,num,0,len(array)-1)
if position== -1:
    print("Element not found")
else:
    print("Using Binary Search: ",position+1)