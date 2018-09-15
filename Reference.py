from pandas import pandas
from Mainwarehouse import Warehouse
from Conveyerbelt2 import conveyerbelt
import NewWarehouse as NW
class Referto:
    
    def __init__(self):
        self.reference = {}
        self.position = ''
        self.ProductID = ''
        self.existingPos = []
        for ids in NW.generateProduct():
            self.ConvertProductID(ids)
    
    def ConvertProductID(self,ID):
        self.ProductID = ID
        if ID[0] in 'ABC':
            self.StoreWarehouse1()
        elif ID[0] in 'DEF':
            self.StoreWarehouse2()
        elif ID[0] in 'GHI':
            self.StoreWarehouse3()
        else:
            self.StoreWarehouse5()
        self.reference[self.ProductID] = self.position
        self.existingPos.append(self.position)

    def StoreWarehouse1(self):
        wnum = 1
        ID = self.ProductID
        self.position = str(wnum) + '0' + str(ID[1]) + '0' + str(ID[2]) + '0' + str(ID[3])

    def StoreWarehouse2(self):
        wnum = 2
        ID = self.ProductID
        self.position = str(wnum) + '0' + str(ID[1]) + '0' + str(ID[2]) + '0' + str(ID[3])

    def StoreWarehouse3(self):
        wnum = 3
        ID = self.ProductID
        self.position = str(wnum) + '0' + str(ID[1]) + '0' + str(ID[2]) + '0' + str(ID[3])

    def StoreWarehouse5(self):
        wnum = 5
        ID = self.ProductID
        self.position = str(wnum) + '0' + str(ID[1]) + '0' + str(ID[2]) + '0' + str(ID[3])
        if self.position in self.existingPos:
            #X shift 10
            self.position = str(wnum) + '0' + str(int(ID[1])) + str(int(ID[2])) + str(int(ID[3]) + 10)
            if self.position in self.existingPos:
            #Y shift 10
                self.position = str(wnum) + '0' + str(int(ID[1])) + str(int(ID[2]) + 10) + '0' + str(int(ID[3]))
                if self.position in self.existingPos:
            #X shift 10 Y shift 10
                    self.position = str(wnum) + '0' + str(int(ID[1])) + str(int(ID[2]) + 10) + str(int(ID[3]) + 10)
                    if self.position in self.existingPos:
            #Row Shift 5
                        self.position = str(wnum) + '0' + str(int(ID[1]) + 5) + '0' + str(ID[2]) + '0' + str(ID[3])
                        if self.position in self.existingPos:
            #Row Shift 5 X shift 10
                            self.position = str(wnum) + '0' + str(int(ID[1]) + 5) + '0' + str(int(ID[2])) + str(int(ID[3]) + 10)
                            if self.position in self.existingPos:
            #Row Shift 5 Y shift 10
                                self.position = str(wnum) + '0' + str(int(ID[1]) + 5) + str(int(ID[2]) + 10) + '0' + str(int(ID[3]))
                                if self.position in self.existingPos:
            #Row Shift 5 Y shift 10 X Shift 10
                                    self.position = str(wnum) + '0' + str(int(ID[1]) + 5) + str(int(ID[2]) + 10) + str(int(ID[3]) + 10)           
                                    if self.position in self.existingPos:
            #Row Shift 10
                                        self.position = str(wnum) + str(int(ID[1]) + 10) + '0' + str(ID[2]) + '0' + str(ID[3])
                                        if self.position in self.existingPos:
            #Row Shift 10 X shift 10
                                            self.position = str(wnum) + str(int(ID[1]) + 10) + '0' + str(int(ID[2])) + str(int(ID[3]) + 10)
                                            if self.position in self.existingPos:
            #Row Shift 10 Y shift 10
                                                self.position = str(wnum) + str(int(ID[1]) + 10) + str(int(ID[2]) + 10) + '0' + str(int(ID[3]))
                                                if self.position in self.existingPos:
            #Row Shift 10 Y shift 10 X Shift 10
                                                    self.position = str(wnum) + str(int(ID[1]) + 10) + str(int(ID[2]) + 10) + str(int(ID[3]) +10)
                                                    if self.position in self.existingPos:
            #Row Shift 15
                                                        self.position = str(wnum) + str(int(ID[1]) + 15) + '0' + str(int(ID[2])) + '0' + str(int(ID[3]))
                                                        if self.position in self.existingPos:
            #Row Shift 15 X shift 10
                                                            self.position = str(wnum) + str(int(ID[1]) + 15) + '0' + str(int(ID[2])) + str(int(ID[3]) + 10)
                                                            if self.position in self.existingPos:
            #Row Shift 15 Y shift 10
                                                                self.position = str(wnum) + str(int(ID[1]) + 15) + str(int(ID[2]) + 10) + '0' + str(int(ID[3]))
                                                                if self.position in self.existingPos:
            #Row Shift 15 Y shift 10 X Shift 10
                                                                    self.position = str(wnum) + str(int(ID[1]) + 15) + str(int(ID[2]) + 10) + str(int(ID[3]) + 10)
            
                
'''c = Referto()
print(c.reference['Y599'])'''