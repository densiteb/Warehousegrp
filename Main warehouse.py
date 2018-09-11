from pandas import pandas
from pprint import pprint
import string
class Warehouse:
    def __init__(self):
        self.warehouse = []
        self.warehouse1 = []
        self.warehouse2 = []
        self.warehouse3 = []
        self.warehouse4 = []
        self.warehouse5 = []


#Creates warehouse 1,2, and 3
    def createWarehouse123(self):
        shelfs = []
        rows = []
        for row in range(10):
            rows.append([])
        for row in range(10):
            shelfs.append(rows)
        for shelf in range(5):
            self.warehouse1.append(shelfs)
            self.warehouse2.append(shelfs)
            self.warehouse3.append(shelfs)
        self.warehouse.append(self.warehouse1)
        self.warehouse.append(self.warehouse2)
        self.warehouse.append(self.warehouse3)
#Creates warehouse 4   
    def createWarehouse4(self):
        shelfs = [''] * 5
        print(shelfs)
        grid = []
        for i in range(5):
            grid.append(shelfs)
        for rows in range(7):
            self.warehouse4.append(grid)
        self.warehouse.append(self.warehouse4)
#Creates warehouse 5
    def createWarehouse5(self):
        shelfs = []
        rows = []
        for row in range(20):
            rows.append([])
        for row in range(20):
            shelfs.append(rows)
        for shelf in range(20):
            self.warehouse5.append(shelfs)
        self.warehouse.append(self.warehouse5)

    def createAllWarehouse(self):
        self.createWarehouse123()
        self.createWarehouse4()
        self.createWarehouse5()


w = Warehouse()
w.createAllWarehouse()
w.warehouse4[0][0].append('65100')
print(pandas.DataFrame(w.warehouse4))



        



        