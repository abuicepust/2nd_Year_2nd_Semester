def sel_srt(mylist):
    for i in range(len(mylist)-1):
        min=i
        for j in range(i+1,len(mylist)):
            if(mylist[j]<mylist[min]):
                min=j
        else:
            mylist[i],mylist[min]=mylist[min],mylist[i]
    return mylist


n=int(input("Enter the how many element: "))
array=list(map(int, input("Enter the elements: ").split()[:n]))
print("You entered: ",array)
sel_srt(array)
print("sorted: ",array)