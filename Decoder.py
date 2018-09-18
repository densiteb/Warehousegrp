class Decoder:
    
    def __init__(self,ProductLocation):
        self.location = ProductLocation
        self.wnum = ProductLocation[0]
        self.rownum = 0
        self.Row = 0
        self.Y = 0
        self.X = 0
        self.slotnum = 0
        self.barcode = ''
        if len(ProductLocation) == 6:
            self.decodeRownum()
        elif len(ProductLocation) >= 8:
            if len(ProductLocation) == 9:
                self.location = ProductLocation[0:4]
                self.encodeslot() 
            elif len(ProductLocation) == 10:
                self.location = ProductLocation[0:5]
                self.encodeslot() 
            elif len(ProductLocation) == 11:
                self.location = ProductLocation[0:6]
                self.encodeslot()   
        else:
            self.decodeRow()
            self.decodeX()
            self.decodeY()
        
        

    
    def decodeRow(self):
        try:
            if self.location[1] == '0':
                self.Row = int(self.location[2]) - 1
                self.decodeSlotnum()
            else:
                self.Row = int(self.location[1:3]) - 1
                self.decodeSlotnum()
        except:
            pass
    def decodeY(self):
        try:
            if self.location[3] == '0':
                self.Y = int(self.location[4])
                self.decodeSlotnum()
            else:
                self.Y = int(self.location[3:5])
                self.decodeSlotnum()
        except:
            pass
        
    
    def decodeX(self):
        try:
            if self.location[5] == '0':
                self.X = int(self.location[6])
                self.decodeSlotnum()
            else:
                self.X = int(self.location[5:7])
                self.decodeSlotnum()
        except:
            pass

    def decodeRownum(self):
        try:
            if self.location[2] == '0':
                self.rownum = int(self.location[3]) - 1
            else:
                self.rownum = int(self.location[2:4]) - 1
        except:
            pass

    def decodeSlotnum(self):
        if self.wnum == '1' or self.wnum == '2' or self.wnum == '3':
            if self.Y == 0:
                self.slotnum = self.X + 1
            else:
                self.slotnum = (10 * (self.Y)) + (self.X +1)
        elif self.wnum == '4':
            if self.Y == 0:
                self.slotnum = self.X + 1
            else:
                self.slotnum = 5 * self.Y  + (self.X + 1)
        elif self.wnum == '5':
            if self.Y == 0:
                self.slotnum = self.X + 1
            else:
                self.slotnum = 20 * self.Y + (self.X + 1)

    def encodeslot(self):
        self.slotnum = self.location[3:]
        try:
            if self.location[1] == '0':
                self.Row = int(self.location[2]) - 1
            else:
                self.Row = int(self.location[1:3]) - 1
            
            if self.wnum == '1' or self.wnum == '2' or self.wnum == '3':
                self.Y = (int(self.location[3:]) - 1) // 10
                self.X = (int(self.location[3:]) - 1) % 10 
                if self.Y == 10 and self.X == 0:
                    self.X = 9
                    self.Y = 9
            elif self.wnum == '4':
                self.Y = (int(self.location[3:]) - 1) // 5
                self.X = (int(self.location[3:]) - 1) % 5 
                if self.Y == 5 and self.X == 0:
                    self.Y = 4
                    self.X = 4
            elif self.wnum == '5':
                self.Y = (int(self.location[3:]) - 1) // 20  
                self.X = (int(self.location[3:]) - 1) % 20
                '''if self.Y == 20 and self.X == 0:
                    self.Y = 19
                    self.X = 19'''
            
            if int(self.location[1]) == 0:
                Row = '0' + str(self.location[2])
            else:
                Row = str(self.location[1:3])

            if self.Y < 10:
                Y = '0' + str(self.Y)
            else:
                Y = self.Y

            if self.X < 10:
                X = '0' + str(self.X)
            else:
                X = self.X
            self.barcode = str(self.wnum) + str(Row) + str(Y) + str(X)
        except:
            pass
 

'''d =Decoder('52010000000')
print(d.wnum,d.Row,d.Y,d.X,d.slotnum,d.barcode)'''


        
        

