# Department of ICE, Pabna University of Science and Technology
# Name: Md. Abu Yousuf
# Roll: 180640
# Session: 2017-2018
# Course Code: ICE-2202
# Course Title: Data Structure and Algorithm Sessional

#1->3 pegs and N disk
#2-> only one move possible at a time from must be top position.
#3-> Every pegs ascending order maintain from top to bottom.
#Now lets start solve this problem using recursion

def Tower_of_hanoi(Disk,First_tower, destination_tower, auxiliary_tower):
    if Disk == 1:
        print("Move disk 1 from First_tower", First_tower, "to destination_tower", destination_tower)
        return
    Tower_of_hanoi(Disk - 1, First_tower, auxiliary_tower, destination_tower)
    print ("Move disk", Disk, "from First_tower", First_tower, "to destination_tower", destination_tower)
    Tower_of_hanoi(Disk - 1, auxiliary_tower, destination_tower, First_tower)


# Driver code
n = int(input("Enter the Number of Disk for Tower of Hanoi : "))
print("Output format for Disk is : ")
Tower_of_hanoi(n, 'A', 'B', 'C')