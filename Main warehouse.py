from pprint import pprint
class Warehouse:
    def __init__(self):
        self.warehouse1= []
        self.warehouse2 = []
        self.warehouse3 = []
        self.warehouse4 = []
        self.warehouse5 = []


#Creates warehouse 1,2, and 3
    def createWarehouse123(self):
        shelfs = []
        rows = []
        for slots in range(10):
            rows.append([])
        for row in range(10):
            shelfs.append(rows)
        for shelf in range(5):
            self.warehouse1.append(shelfs)
            self.warehouse2.append(shelfs)
            self.warehouse3.append(shelfs)
w = Warehouse()
w.createWarehouse123()
pprint(w.warehouse1)
        



        