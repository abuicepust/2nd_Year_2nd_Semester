
def first_pattern (pattern,Text):
    l1=len(pattern)
    l2=len(Text)
    for i in range (l2-l1+1):
        j=0;
        while (j < l1):
            if(Text[i+j] != pattern[j]):
                break
            j+=1
        if(j==l1):
            print(f"find matching pattern index is {i}")


while True:
    value=int(input("Do you want to continue this program:\n1.YES\n 2.No\n"))
    if(value==1):
        Text, pattern = input("ENter two string : ").split()
        first_pattern(pattern, Text)
    else:
        print("The end :")



