from Conveyerbelt2 import conveyerbelt
from Mainwarehouse import Warehouse
import string

class Commands:
    
    def __init__(self):
        self.Code = ''
        self.c = conveyerbelt()
        self.w = Warehouse()
        self.w.createAllWarehouse()
        self.command()

    def command(self):
        command = input('Please enter a command: ')
        self.Code = command.upper()
        if self.Code == 'LEAVE':
            return(0)
        self.DetectCommands()

    def VerifyCommand(self):
        letters = string.ascii_uppercase.replace('Z','')
        Verify = list(self.Code)
        self.DetectCommands()
        #else
        print('Input is invalid.Please enter a new command.')

    def DetectCommands(self):
        Code = self.Code[0]
        if Code == '0':
            self.Retrieve()
        elif Code == '1':
            self.Store()
        elif Code == '2':
            self.Sort()
        elif Code == '3':
            self.RetrieveBelt()
        elif Code == '4':
            self.Output()
        elif Code == '5':
            self.Search()
        elif Code == '9':
            self.Manual()
        else:
            print('Command is not recognized')
            self.command()

    def Retrieve(self):
         print('ok0')

    def Store(self):
        ware = self.w
        w = ord(self.Code[1])
        r = int(self.Code[2]) - 1
        y = int(self.Code[3])
        x = int(self.Code[4])
        if w >= ord('A') and w <= ord('C'):
            ware.warehouse1[r][y][x] = str(self.Code[1:5])
        if ord(self.Code[1]) >= ord('J'):
            ware.warehouse5[r][y][x] = str(self.Code[1:5])
        
        self.command()


            
            

    
    def Sort(self):
        print('ok2')

    def RetrieveBelt(self):
        if self.Code == '30000':
            if self.c.size() > 0:
                print('Retrieve a product with id ' + self.c.retrievebelt() + ' from the belt.')
                print('The belt now has ' + str(self.c.size()) + ' products on the line.')
            elif self.c.size() <= 0:
                print('The belt is empty. Cannot retrieve product from the belt.')
        else:
            print('Command is not recognized')

    def Output(self):
        if self.Code == '40000':
            self.w.outputwarehouse()
        else:
            print('Command is not recognized')
        self.command()
    
    def Search(self):
        print('ok5')

    def Manual(self):
        print('ok9')

c = Commands()

