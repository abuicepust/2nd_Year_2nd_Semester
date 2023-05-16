# Department of ICE, Pabna University of Science and Technology
# Name: Md. Abu Yousuf
# Roll: 180640
# Session: 2017-2018
# Course Code: ICE-2202
# Course Title: Data Structure and Algorithm Sessional

#Pattern matching find using naive algorithm.

def Naive_search(Pattern,Text):
    M = len(Pattern)
    N = len(Text)
    for i in range(N - M + 1):
        j = 0
        while (j < M):
            if (Text[i + j] != Pattern[j]):
                break
            j += 1

        if (j == M):
            print("Pattern Matching found at index  ", i)
#function close
#Test code for above function
Text, Pattern = input("Enter String  first pattern then Text : ").split()
Naive_search(Pattern, Text)