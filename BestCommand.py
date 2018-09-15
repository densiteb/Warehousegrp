from Conveyerbelt2 import conveyerbelt
from Mainwarehouse import Warehouse
from robotarm import Barcode
from Decoder import Decoder
import string

class Commands:
    
    def __init__(self):
        self.Code = ''
        self.c = conveyerbelt()
        self.w = Warehouse()
        self.w.createAllWarehouse()
        self.b = Barcode()
        self.command()

    def command(self):
        command = input('Please enter a command: ')
        self.Code = command.upper()
        if self.Code == 'LEAVE':
            return(0)
        self.__VerifyCommand__()

    def __VerifyCommand__(self):
        letters = string.ascii_uppercase.replace('Z','')
        Verify = list(self.Code)
        if len(self.Code) == 0:
            print('No command.')
            self.command()
        self.DetectCommands()

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
        ware = self.w
        productid = self.Code[1:]
        if self.c.size == 10:
            print('Belt is full.Cannot retrieve product.')
            self.command()
        elif productid not in self.b.memory:
            print('Product does not exist.Cannot retrieve the product.')
            self.command()
        position = self.b.memory[productid]
        if position == 'On the belt':
            print('Product is on the belt.')
            self.command()
        d = Decoder(position)
        if position[0] == '1':
            ware.warehouse1[d.Row][d.Y][d.X] = ''
            self.b.existingPos.remove(position)
            self.b.memory[productid] = 'On the belt'
            print('Moving from Belt to A')
            print('Getting a product id ' + productid + ' in Warehouse A: row '+ str(int(d.Row)) + ' slot ' + str(d.X))
            print('Moving from A to Start')
            print('Placing product id ' + productid + ' on the belt. ')
            print('Retrieving Successfully!')
            self.c.insert(productid)
        elif position[0] == '2':
            ware.warehouse2[d.Row][d.Y][d.X] = ''
            self.b.existingPos.remove(position)
            self.b.memory[productid] = 'On the belt'
            print('Moving from Belt to A')
            print('Moving from A to B')
            print('Getting a product id ' + productid + ' in Warehouse B: row '+ str(int(d.Row)) + ' slot ' + str(d.X))
            print('Moving from B to A')
            print('Moving from A to Start')
            print('Placing product id ' + productid + ' on the belt. ')
            print('Retrieving Successfully!')
            self.c.insert(productid)
        elif position[0] == '3':
            ware.warehouse3[d.Row][d.Y][d.X] = ''
            self.b.existingPos.remove(position)
            self.b.memory[productid] = 'On the belt'
            print('Moving from Belt to A')
            print('Moving from A to C')
            print('Getting a product id ' + productid + ' in Warehouse C: row '+ str(int(d.Row)) + ' slot ' + str(d.X))
            print('Moving from C to A' )
            print('Moving from A to Start')
            print('Placing product id ' + productid + ' on the belt. ')
            print('Retrieving Successfully!')
            self.c.insert(productid)
        elif position[0] == '4':
            ware.warehouse4[d.Row][d.Y][d.X] = ''
            self.b.existingPos.remove(position)
            self.b.memory[productid] = 'On the belt'
            print('Moving from Belt to A')
            print('Moving from A to B')
            print('Moving from B to D')
            print('Getting a product id ' + productid + ' in Warehouse D: row '+ str(int(d.Row)) + ' slot ' + str(d.X))
            print('Moving from D to B')
            print('Moving from B to A')
            print('Moving from A to Start')
            print('Placing product id ' + productid + ' on the belt. ')
            print('Retrieving Successfully!')
            self.c.insert(productid)
        elif position[0] == '5':
            ware.warehouse5[d.Row][d.Y][d.X] = ''
            self.b.existingPos.remove(position)
            self.b.memory[productid] = 'On the belt'
            print('Moving from Belt to A')
            print('Moving from A to B')
            print('Moving from B to E')
            print('Getting a product id ' + productid + ' in Warehouse E: row '+ str(int(d.Row)) + ' slot ' + str(d.X))
            print('Moving from E to B')
            print('Moving from B to A')
            print('Moving from A to Start')
            print('Placing product id ' + productid + ' on the belt. ')
            print('Retrieving Successfully!')
            self.c.insert(productid)
        self.command()


    def Store(self):
        ware = self.w
        productid = self.Code[1:]
        if productid in self.b.memory:
            print('Product already exists.Cannot store the product.')
            self.command()
        self.b.ConvertProductID(productid)
        if productid not in self.b.memory:
            print('Slot is occupied.Cannot store the product.')
            self.command()
        position = self.b.memory[productid]
        d = Decoder(position)
        if position[0] == '1':
            ware.warehouse1[d.Row][d.Y][d.X] = productid
            print('Moving from Belt to A')
            print('Storing a product id ' + productid + ' in Warehouse A: row '+ str(int(d.Row)) + ' slot ' + str(d.X))
            print('Moving from A to Start')
            print('Storing Successfully!')
        elif position[0] == '2':
            ware.warehouse2[d.Row][d.Y][d.X] = productid
            print('Moving from Belt to A')
            print('Moving from A to B')
            print('Storing a product id ' + productid + ' in Warehouse B: row '+ str(int(d.Row)) + ' slot ' + str(d.X))
            print('Moving from B to A')
            print('Moving from A to Start')
            print('Storing Successfully!')
        elif position[0] == '3':
            ware.warehouse3[d.Row][d.Y][d.X] = productid
            print('Moving from Belt to A')
            print('Moving from A to C')
            print('Storing a product id ' + productid + ' in Warehouse C: row '+ str(int(d.Row)) + ' slot ' + str(d.X))
            print('Moving from C to A' )
            print('Moving from A to Start')
            print('Storing Successfully!')
        elif position[0] == '4':
            ware.warehouse4[d.Row][d.Y][d.X] = productid
            print('Moving from Belt to A')
            print('Moving from A to B')
            print('Moving from B to D')
            print('Storing a product id ' + productid + ' in Warehouse D: row '+ str(int(d.Row)) + ' slot ' + str(d.X))
            print('Moving from D to B')
            print('Moving from B to A')
            print('Moving from A to Start')
            print('Storing Successfully!')
        elif position[0] == '5':
            ware.warehouse5[d.Row][d.Y][d.X] = productid
            print('Moving from Belt to A')
            print('Moving from A to B')
            print('Moving from B to E')
            print('Storing a product id ' + productid + ' in Warehouse E: row '+ str(int(d.Row)) + ' slot ' + str(d.X))
            print('Moving from E to B')
            print('Moving from B to A')
            print('Moving from A to Start')
            print('Storing Successfully!')
        self.command()
    
    def Sort(self):
        print('ok2')

    def RetrieveBelt(self):
        if self.Code == '30000':
            if self.c.size() > 0:
                print('Retrieve a product with id ' + self.c.items[-1] + ' from the belt.')
                self.c.retrievebelt()
                print('The belt now has ' + str(self.c.size()) + ' products on the line.')
                del self.b.memory[self.c.retrievebelt()]
            elif self.c.size() <= 0:
                print('The belt is empty. Cannot retrieve product from the belt.')
        else:
            print('Command is not recognized')
        self.command()

    def Output(self):
        if self.Code == '40000':
            self.w.outputwarehouse()
        else:
            print('Command is not recognized')
        self.command()
    
    def Search(self):
        if self.b.memory[self.Code[1:]]:
            position = self.b.memory[self.Code[1:]]
            d = Decoder(position)
            print('Found product at Warehouse:' + str(d.wnum) + ' Row:' + str(d.Row) + ' X:' + str(d.X) + ' Y:' + str(d.Y)) 
    
    def Manual(self):
        print('ok9')

c = Commands()

