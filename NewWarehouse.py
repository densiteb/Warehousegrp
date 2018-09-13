import string
class ProductID:

   def __init__(self):
        self.alpha = string.ascii_uppercase.replace('Z','')
        self.alphab = ''
        self.wnum = 0
        self.firstnum = 0
        self.secondnum = 0
        self.productid = []
        self.convertedid = []
        self.hashindex = []

    def GenerateProductID(self):
        for first in self.alpha:
            alphab = first
            wnum = 0
            firstnum = -1
            secondnum = -1
            for ware in range(5):
                wnum += 1
                for loation in range(10):
                    firstnum += 1
                    for locate in range(10):
                        secondnum += 1
                        self.productid.append(first + str(self.wnum) + str(self.firstnum) + str(self.secondnum))
                        self.convertedid.append(str(ord(first)) + str(self.wnum) + str(self.firstnum) + str(self.secondnum))
                    self.secondnum = -1
                self.firstnum = -1

    def hashProduct(self):
        for ids in self.convertedid:
            ids = int(ids)
            if ids >= 84275:
                ids = ids-65%19
                if ids in self.hashindex():
                    ids = ids-65%19
            else:
                self.hashindex.append(ids)
 #-65%19 hash function
p = ProductID()
p.GenerateProductID()
p.hashProduct()
print(len(p.hashindex))

    