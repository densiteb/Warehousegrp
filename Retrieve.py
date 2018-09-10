def Retrieve(x):
    i = 0
    robot = []
    Belt = [robot]
    Warehouse1 = ["0A101", "0A120", "0A302", 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Warehouse2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Warehouse5 = [0, 0, 0, 0, 0, 0, 0, "0A302", 0, "0A102", 0, 0, 0, 0, 0]
    Warehouse1.append(robot)
    Belt.remove(robot)
    Warehouse2.append(robot)
    Warehouse1.remove(robot)
    Warehouse5.append(robot)
    Warehouse2.remove(robot)
    a = Warehouse5.index("0A102")
    robot.append(Warehouse5[a])
    Belt.append(robot)
    return Belt
print (Retrieve(10))

    
    
    
