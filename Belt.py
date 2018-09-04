def MoveToBelt(x):
    belt =[] 
    i = 0
    while i <1:
        x = input("Input Product ID:").upper()
        if len(belt) < 10:
            belt.append(x)
        elif len(belt) >= 10:
            print ("full")
            print(belt)
            break   
    return belt
MoveToBelt(1)



def  MoveOutFromBelt(x):
    belt = [0,1,2,3,4,5,6,7,8,9]
    slot = []
    i = 0
    while i<1:
        x = input("Input Product ID:").upper()
        if x == "STOP":
            print ("check69")
            if len(belt) != 0:
                slot.append(belt[0])
                belt.remove(belt[0])
                print(slot)
                print (belt)
            elif len(belt) == 0:
                print ("unavailable")
                print (slot)
                break
    return slot
MoveOutFromBelt(1)        





 
        