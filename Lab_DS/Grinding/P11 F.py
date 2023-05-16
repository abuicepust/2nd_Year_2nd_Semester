

import numpy as np
def knap_sack(Capacity,profit,weight,item):
    Matrix=[[0 for x in range(Capacity+1)] for y in range(item+1)]
    #table for problem
    for i in range(item+1):
        for w in range(Capacity+1):
            if i==0 or w==0:
                Matrix[i][w]=0
            elif weight[i-1] <= w:
                Matrix[i][w]=max(profit[i-1]+Matrix[i-1][w-weight[i-1]],Matrix[i-1][w])
            else:
                Matrix[i][w]=Matrix[i-1][w]
    lis = np.array(Matrix)
    print(f"The matrix for 0/n knapsack :")
    print(lis)
    print(f"The maximum profit is : {lis[item][Capacity]}")
item = int(input("Enter the number of item : " ))
profit = [int(item) for item in input("Enter the profit value : ").split()]
weight = [int(item) for item in input("Enter the weight value : ").split()]
Capacity = int(input("Enter number of capacity : " ))
knap_sack(Capacity,profit,weight,item)
