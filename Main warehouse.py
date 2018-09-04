from pandas import pandas
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
        shelfs = []
        rows = {}
        for slots in range(10):
            rows[hash(ord('a'))] = 'milk'
        for row in range(10):
            shelfs.append(rows)
        for shelf in range(5):
            self.warehouse1.append(shelfs)
            self.warehouse2.append(shelfs)
            self.warehouse3.append(shelfs)
#Creates warehouse 4   
    def createWarehouse4(self):
        shelfs = []
        rows = {}
        for row in range(5):
            shelfs.append(rows)
        for shelf in range(7):
            self.warehouse4.append(shelfs)
#Creates warehouse 5
    def createWarehouse5(self):
        shelfs = []
        rows = []
        for slots in range(20):
            rows.append([])
        for row in range(20):
            shelfs.append(rows)
        for shelf in range(20):
            self.warehouse5.append(shelfs)

    def createAllWarehouse(self):
        self.createWarehouse123()
        self.createWarehouse4()
        self.createWarehouse5()  

w = Warehouse()
w.createAllWarehouse()
print(pandas.DataFrame(w.warehouse4))
print((ord('G')+ord('4')+ord('8')+ord('8'))-65//3)
print(string.ascii_uppercase)
        



        