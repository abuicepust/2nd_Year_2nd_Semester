def kanpsack(Capacity, weights, profits, n):
    if n == 0 or Capacity == 0:
        return 0
    if weights[n - 1] > Capacity:
        return kanpsack(Capacity, weights, profits, n - 1)
    else:
        return max(profits[n - 1] + kanpsack(Capacity - weights[n - 1], weights, profits, n - 1),
                   kanpsack(Capacity, weights, profits, n - 1))


print("Enter the profits: ")
profits = list(map(int, input().split()))
print("Enter the weights: ")
weights = list(map(int, input().split()))
Capacity = int(input("Enter the capacity: "))
n = len(weights)
print('Maximum profit:',kanpsack(Capacity, weights, profits, n))
