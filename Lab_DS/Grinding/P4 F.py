def Binary_search(list, num, start, end):
    if start>end:
        return -1
    mid=(start+end)//2
    if(num==list[mid]):
        return mid
    if(num<list[mid]):
        return Binary_search(list, num, start, mid - 1)
    if(num>list[mid]):
        return Binary_search(list, num, mid + 1, end)


n=int(input("Enter the number of elements: "))
Array=list(map(int, input("Enter the elements: ").split()[:n]))
print("The elements: ",Array)
num=int(input("Enter the number to search: "))
position= Binary_search(Array,num,0,len(Array)-1)
if position==-1:
    print("Not Found")
else:
    print("Found at",position+1)