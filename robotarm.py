from pandas import pandas
from Mainwarehouse import Warehouse
from Conveyerbelt2 import conveyerbelt
class RobotArm:
    
    def __init__(self):
        self.memory = {}
        self.position = ''
        self.ProductID = ''
        self.existingPos = []
    def ConvertProductID(self,ID):
        self.ProductID = ID
        wnum = 0
        rr = 0
        yy = 0
        xx = 0
        if ID[0] in 'ABC':
            wnum = 1
            self.position = str(wnum) + '0' + str(ID[1]) + '0' + str(ID[2]) + '0' + str(ID[3])
            if self.position in self.existingPos:
                self.Sameposition()
        elif ID[0] in 'DEF':
            wnum = 2
        elif ID[0] in 'GHI':
            wnum = 3
        else:
            wnum = 5
        if self.position not in self.existingPos:
            self.memory[self.ProductID] = self.position
            self.existingPos.append(self.position)
            print('Storing successful')

    def Sameposition(self):
        ID = self.ProductID
        wnum = 4
        self.position = str(wnum) + '0' + str(ID[1]) + '0' + str(ID[2]) + '0' + str(ID[3])
        if self.position in self.existingPos:
            print('Slot is occupied.Cannot store the product.')
            
                
                



c = RobotArm()
c.ConvertProductID('A125')
c.ConvertProductID('B125')
c.ConvertProductID('C125')
print(c.memory)


    
        

        
        
        
        