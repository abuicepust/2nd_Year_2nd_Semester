import numpy as pip


def knapsack(Capacity, Profit, Weight, Item):
    Matrix = [[0 for x in range(Capacity + 1)] for y in range(Item + 1)]

    for i in range(Item + 1):
        for w in range(Capacity + 1):
            if i==0 or w==0:
                Matrix[i][w]=0
            elif Weight[i-1] <= w:
                Matrix[i][w] = max(Matrix[i - 1][w], Profit[i - 1] + Matrix[i - 1][w - Weight[i - 1]])
            else:
                Matrix[i][w] = Matrix[i - 1][w]

    list = pip.array(Matrix)
    print("The Matrix 0/1 Knapsack: ")
    print(list)
    print("Maximum profit: ", list[Item][Capacity])


Item = int(input("Enter how mnay Item: "))
Profit = [int(Item) for Item in (input("Enter the profits: ").split())]
Weight = [int(Item) for Item in (input("Enter weights: ").split())]
Capacity = int(input("Enter the capacity: "))
knapsack(Capacity, Profit, Weight, Item)
