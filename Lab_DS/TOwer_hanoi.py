#Maintain two step
def tower_hanoi (disk,beg,end,aux):
    if disk==1:
        print(f"Move disk {disk} from tower {beg} to tower{end}")
        return
    tower_hanoi(disk-1,beg,aux,end)
    print(f"Move disk{disk} from tower {beg} to tower{end} ")
    tower_hanoi(disk-1,aux,end,beg)
disk=int(input("Enter the number of disk : "))
tower_hanoi(disk,'A','B','C')
