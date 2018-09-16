from pandas import pandas
from pprint import pprint
import numpy
import string
class Warehouse:
    def __init__(self):
        self.warehouse1 = []
        self.warehouse2 = []
        self.warehouse3 = []
        self.warehouse4 = []
        self.warehouse5 = []


#Creates warehouse 1,2, and 3
    def createWarehouse123(self):
        self.warehouse1 = [[[ '0' for x in range(10)] for y in range(10)]for z in range(5)]
        self.warehouse2 = [[[ '0' for x in range(10)] for y in range(10)]for z in range(5)]
        self.warehouse3 = [[[ '0' for x in range(10)] for y in range(10)]for z in range(5)]
#Creates warehouse 4   
    def createWarehouse4(self):
        self.warehouse4 = [[[ '0' for x in range(5)] for y in range(5)]for z in range(7)]
        
#Creates warehouse 5
    def createWarehouse5(self):
        self.warehouse5 = [[[ '0' for x in range(20)] for y in range(20)]for z in range(20)]

    def createAllWarehouse(self):
        self.createWarehouse123()
        self.createWarehouse4()
        self.createWarehouse5()
    
    def outputwarehouse(self):
        print(pandas.DataFrame(self.warehouse1))
        print(pandas.DataFrame(self.warehouse2))
        print(pandas.DataFrame(self.warehouse3))
        print(pandas.DataFrame(self.warehouse4))
        print(pandas.DataFrame(self.warehouse5))

'''w = Warehouse()
w.createAllWarehouse()
w.warehouse5[19][19][19] = 'Y599'
w.outputwarehouse()'''




        



        