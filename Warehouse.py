class Warehouse:
    def __init__(self,xd,yd,row):
        self.xd = xd
        self.yd = yd
        self.row = row
        self.wareh = {}
        self.warehouse6 = {}
        self.shelf = [self.wareh]
        self.alphabet1 =  "ABC"
        self.alphabet2 = "DEF"
        self.alphabet3 = "GHI"
        self.alphabet5 = "JKLMNOPQRSTUVWXY"
    def createwarehouse(self):
        yz = 100
        numalphabet = 0
        count4part1to2to3 = 1
        part = 1
        count1 = 0
        for i in range(self.row):
            for j in range(self.yd):
                for k in range(self.xd):
                    if self.xd == 10 and self.yd == 10 and self.row == 5:
                        self.wareh["A_I"+str(yz)] = "none"
                        yz += 1
                        if yz == 600:
                            yz = 100
                    elif self.xd == 5 and self.yd == 5 and self.row == 7:
                        if part == 1:
                            self.wareh["W1S"+str(yz)] = "none"
                            count4part1to2to3 += 1
                            yz += 1
                            if count4part1to2to3 == 51:
                                part = 2
                                yz =100
                        elif part == 2:
                            self.wareh["W2S"+str(yz)] = "none"
                            count4part1to2to3 += 1
                            yz += 1
                            if count4part1to2to3 == 101:
                                part = 3
                                yz = 100
                        elif part == 3:
                            self.wareh["W3S"+str(yz)] = "none"
                            yz += 1
                    elif  self.xd == 20 and self.yd == 20 and self.row == 20:
                        self.wareh[self.alphabet5[numalphabet]+str(yz)] = "none"
                        yz += 1
                        if yz == 600:
                            yz = 100
                            numalphabet+=
                            
    

                        

                        
                    
    def displaywarehouse(self):
        print(self.shelf)


w1 = Warehouse(10,10,5) ;w2 = Warehouse(10,10,5);w3 = Warehouse(10,10,5) ;w4 = Warehouse(5,5,7) ;w5 = Warehouse(20,20,20)

w1.createwarehouse();w2.createwarehouse();w3.createwarehouse();w4.createwarehouse();w5.createwarehouse()
w5.displaywarehouse()
