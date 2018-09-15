class Decoder:
    
    def __init__(self,ProductLocation):
        self.location = ProductLocation
        self.wnum = ProductLocation[0]
        self.Row = 0
        self.Y = 0
        self.X = 0
        self.decodeRow()
        self.decodeX()
        self.decodeY()

    
    def decodeRow(self):
        if self.location[1] > self.location[2]:
            self.Row = int(self.location[1:3]) - 1
        else:
            self.Row = int(self.location[2]) - 1

    def decodeY(self):
        if self.location[3] == '0':
            self.Y = int(self.location[4])
        else:
            self.Y = int(self.location[3:5])
    
    def decodeX(self):
        if self.location[5] == '0':
            self.X = int(self.location[6])
        else:
            self.X = int(self.location[5:7])

'''d=Decoder('5201919')
print(d.wnum,d.Row,d.Y,d.X)'''






        
        

