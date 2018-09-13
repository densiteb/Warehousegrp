import Conveyerbelt2
class winput:
    def __init__(self , _ID):
        self.command=_ID
        self.robot = []
        self.belt = [robot]
    def Scan(self,link):
        if self.command[0] == "0":
            link.Retrieve(link)
        elif self.command[0] == "1":
            link.Store(link)
        elif self.command[0] == "2":
            link.Sort(link)
        elif self.command[0] == "3":
            link.RetrieveConveyor(link)
        elif self.command[0] == "4":
            link.OutputInformation(link)
        elif self.command[0] == "5":
            link.Search(link)
        elif self.command[0] == "9":
            link.Maunual(link)
    
    def Retrieve(self , link):
        #if retrieve warehouse1:
            self.belt.remove(self.robot)
            self.warehouse1.append(self.robot)
            if  '''Product ID''' in self.warehouse1:
                product = self.warehouse1.index(#Product ID)
                self.robot.append(self.warehouse1[product])
                self.warehouse1.remove(self.robot)
                #จำเป็นต้องแสดงไหมว่าเดินไปเก็บสินค้า
                '''if range(belt)<10:
                    self.belt.append(robot[0])
                    robot = []
                    self.append(self.robot)
                elif range(belt) == 10: 
                    print ("Found the Product at :" xxxx)
                else:
                    print ("Product not found")'''
            else:
                self.warehouse1.remove(self.robot)
                self.belt.append(self.robot)
        #elif retrieve warehouse2:
            self.belt.remove(self.robot)
            self.warehouse1.append(self.robot)
            self.warehouse1.remove(self.robot)
            self.warehouse2.append(self.robot)
            if  '''Product''' ID in Warehouse4:
                product = self.warehouse2.index(#Product ID)
                self.robot.append(self.warehouse2[product])
                self.warehouse2.remove(self.warehouse2[product])
                self.warehouse2.insert(prodduct,"none")
                self.warehouse2.remove(self.robot)
                self.warehouse1.append(self.robot)
                self.warehouse1.remove(self.robot)
                #จำเป็นต้องแสดงไหมว่าเดินไปเก็บสินค้า
                '''if range(belt)<10:
                    self.belt.append(robot[0])
                    robot = []
                    self.belt.append(self.robot)
                elif range(belt) == 10: 
                    print ("Found the Product at :" xxxx)
                else:
                    print ("Product not found")'''
            else:
                self.warehouse2.remove(self.robot)
                self.warehouse1.append(self.robot)
                self.warehouse1.remove(self.robot)
                self.belt.append(self.robot)
        #elif retrieve warehouse3:
            self.belt.remove(self.robot)
            self.warehouse1.append(self.robot)
            self.warehouse1.remove(self.robot)
            self.warehouse3.append(self.robot)
            if  '''Product''' ID in Warehouse4:
                product = self.warehouse3.index(#Product ID)
                self.robot.append(self.warehouse3[product])
                self.warehouse3.remove(self.warehouse3[product])
                self.warehouse3.insert(prodduct,"none")
                self.warehouse3.remove(self.robot)
                self.warehouse1.append(self.robot)
                self.warehouse1.remove(self.robot)
                #จำเป็นต้องแสดงไหมว่าเดินไปเก็บสินค้า
                '''if range(belt)<10:
                    self.belt.append(robot[0])
                    robot = []
                    self.belt.append(self.robot)
                elif range(belt) == 10: 
                    print ("Found the Product at :" xxxx)
                else:
                    print ("Product not found")'''
            else:
                self.warehouse3.remove(self.robot)
                self.warehouse1.append(self.robot)
                self.warehouse1.remove(self.robot)
                self.belt.append(self.robot)
        #elif retrieve warehouse4:
            self.belt.remove(self.robot)
            self.warehouse1.append(self.robot)
            self.warehouse1.remove(self.robot)
            self.warehouse2.append(self.robot)
            self.warehouse2.remove(self.robot)
            self.warehouse4.append(self.robot)
            if  '''Product''' ID in Warehouse4:
                product = self.warehouse4.index(#Product ID)
                self.robot.append(self.warehouse[product])
                self.warehouse4.remove(self.warehouse4[product])
                self.warehouse4.insert(product,"none")
                self.warehouse4.remove(self.robot)
                self.warehouse2.append(self.robot)
                self.warehouse2.remove(self.robot)
                self.warehouse1.append(self.robot)
                self.warehouse1.remove(self.robot)
                #จำเป็นต้องแสดงไหมว่าเดินไปเก็บสินค้า
                '''if range(belt)<10:
                    self.belt.append(robot[0])
                    robot = []
                    self.beltappend(self.robot)
                elif range(belt) == 10: 
                    print ("Found the Product at :" xxxx)
                else:
                    print ("Product not found")'''
            else:
                self.warehouse4.remove(self.robot)
                self.warehouse2.append(self.robot)
                self.warehouse2.remove(self.robot)
                self.warehouse1.append(self.robot)
                self.warehouse1.remove(self.robot)
                self.belt.append(self.robot)
        #elif retrieve warehouse5:
            self.belt.remove(self.robot)
            self.warehouse1.append(self.robot)
            self.warehouse1.remove(self.robot)
            self.warehouse2.append(self.robot)
            self.warehouse2.remove(self.robot)
            self.warehouse5.append(self.robot)
            if  '''Product''' ID in Warehouse5:
                product = self.warehouse5.index(#Product ID)
                self.robot.append(self.warehouse5[product])
                self.warehouse5.remove(self.warehouse5[product])
                self.warehouse5.insert(prodduct,"none")
                self.warehouse5.remove(self.robot)
                self.warehouse2.append(self.robot)
                self.warehouse2.remove(self.robot)
                self.warehouse1.append(self.robot)
                self.warehouse1.remove(self.robot)
                #จำเป็นต้องแสดงไหมว่าเดินไปเก็บสินค้า
                '''if range(belt)<10:
                    self.belt.append(robot[0])
                    robot = []
                    self.belt.append(self.robot)
                elif range(belt) == 10: 
                    print ("Found the Product at :" xxxx)
                else:
                    print ("Product not found")'''
            else:
                self.warehouse5.remove(self.robot)
                self.warehouse2.append(self.robot)
                self.warehouse2.remove(self.robot)
                self.warehouse1.append(self.robot)
                self.warehouse1.remove(self.robot)
                self.belt.append(self.robot)
            
    def Store(self , link):
        #if Store warehouse1:
            self.belt.remove(self.robot)
            self.warehouse1.append(self.robot)
            #################################
            self.warehouse1.remove(self.robot)
            
    def Sort(self , link):
        print ("Sort")
    def RetrieveConveyor(self , link):
        print ("RetrieveConveyor")
    def OutputInformation(self , link):
        print ("OutputInformation")
    def Search(self , link):
        print ("Search")
    def Maunual(self , link):
        print ("Maunual")


link = winput("1A125")
link.Scan(link)
