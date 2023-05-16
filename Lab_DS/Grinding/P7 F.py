def Naive_search(Pattern,Text):
    P = len(Pattern)
    T = len(Text)
    for i in range(T - P + 1):
        j = 0
        while (j < P):
            if (Text[i + j] != Pattern[j]):
                break
            j += 1

        if (j == P):
            print("Pattern Matching found at index  ", i)


Text, Pattern = input("Enter String  first pattern then Text : ").split()
Naive_search(Pattern, Text)
