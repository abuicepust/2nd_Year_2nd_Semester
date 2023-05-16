def TowerOfHanoi(n,source,des,mid):
    if (n<1):
        print("Not possible")
        return
    if (n==1):
        print("Move disk {} From {} to {}".format(n,source,des))
        return
    TowerOfHanoi(n-1,source,mid,des)
    print("Move disk {} from {} To {}".format(n,source,des))
    TowerOfHanoi(n-1,mid,des,source)




n=int(input("Enter the number of disk: "))
TowerOfHanoi(n,"Source","Destinatio","Auxilary")
