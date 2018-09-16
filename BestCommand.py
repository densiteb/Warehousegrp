from Conveyerbelt2 import conveyerbelt
from Mainwarehouse import Warehouse
from robotarm import Barcode
from Decoder import Decoder
from Reference import Referto
import string

class Commands:
    
    def __init__(self):
        self.Code = ''
        self.alpha = string.ascii_uppercase.replace('Z','')
        self.c = conveyerbelt()
        self.w = Warehouse()
        self.w.createAllWarehouse()
        self.b = Barcode()
        self.ref = Referto()
        self.command()

    def command(self):
        command = input('Please enter a command: ')
        self.Code = command.upper()
        if self.Code == 'HELP':
            self.help()
        elif self.Code == 'LEAVE':
            self.leave()
        elif self.Code == 'EXAMPLES':
            self.examples()
        else:
            self.__VerifyCommand__()

    def __VerifyCommand__(self):
        if len(self.Code) == 0:
            print('No command. Use help.')
            self.command()
        else:
            self.DetectCommands()

    def DetectCommands(self):
        Code = self.Code[0]
        if Code == '0' and len(self.Code) == 5 and self.Code[1] in self.alpha and self.Code[2:].isdigit():
            self.Retrieve()
        elif Code == '1' and len(self.Code) == 5 and self.Code[1] in self.alpha and self.Code[2:].isdigit():
            self.Store()
        elif Code == '2' and len(self.Code) == 6 and self.Code[4] == '0' and self.Code[5] == '0' and self.Code.isdigit():
            self.Sort()
        elif Code == '3':
            self.RetrieveBelt()
        elif Code == '4':
            self.Output()
        elif Code == '5' and len(self.Code) == 5 and self.Code[1] in self.alpha and self.Code[2:].isdigit():
            self.Search()
        elif Code == '9' and len(self.Code) == 12 and self.Code[1] in self.alpha:
            self.Manual()
        else:
            print('Command is not recognized.')
            self.help()
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
            self.c.inserttobelt(productid)
            self.command()
        
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
            self.c.inserttobelt(productid)
            self.command()
        
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
            self.c.inserttobelt(productid)
            self.command()
        
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
            self.c.inserttobelt(productid)
            self.command()
        
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
            self.c.inserttobelt(productid)
            self.command()
        
        else:
            self.help()
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

        if position[0] == '1' and d.Row in range(5) and d.Y in range(10) and d.X in range(10):
            ware.warehouse1[d.Row][d.Y][d.X] = productid
            print('Moving from Belt to A')
            print('Storing a product id ' + productid + ' in Warehouse A: row '+ str(int(d.Row)) + ' slot ' + str(d.X))
            print('Moving from A to Start')
            print('Storing Successfully!')
            self.command()

        elif position[0] == '2' and d.Row in range(5) and d.Y in range(10) and d.X in range(10):
            ware.warehouse2[d.Row][d.Y][d.X] = productid
            print('Moving from Belt to A')
            print('Moving from A to B')
            print('Storing a product id ' + productid + ' in Warehouse B: row '+ str(int(d.Row)) + ' slot ' + str(d.X))
            print('Moving from B to A')
            print('Moving from A to Start')
            print('Storing Successfully!')
            self.command()

        elif position[0] == '3' and d.Row in range(5) and d.Y in range(10) and d.X in range(10):
            ware.warehouse3[d.Row][d.Y][d.X] = productid
            print('Moving from Belt to A')
            print('Moving from A to C')
            print('Storing a product id ' + productid + ' in Warehouse C: row '+ str(int(d.Row)) + ' slot ' + str(d.X))
            print('Moving from C to A' )
            print('Moving from A to Start')
            print('Storing Successfully!')
            self.command()

        elif position[0] == '4' and d.Row in range(7) and d.Y in range(6) and d.X in range(6):
            ware.warehouse4[d.Row][d.Y][d.X] = productid
            print('Moving from Belt to A')
            print('Moving from A to B')
            print('Moving from B to D')
            print('Storing a product id ' + productid + ' in Warehouse D: row '+ str(int(d.Row)) + ' slot ' + str(d.X))
            print('Moving from D to B')
            print('Moving from B to A')
            print('Moving from A to Start')
            print('Storing Successfully!')
            self.command()

        elif position[0] == '5' and d.Row in range(20) and d.Y in range(20) and d.X in range(20):
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

        else:
            print('Format invalid.')
            self.command()
    
    def Sort(self):
        ware = self.w
        warenum = self.Code[1]
        d = Decoder(self.Code)
        ref = self.ref.reference
        rownum = d.rownum
        products = []
        if warenum == '1' and rownum in range(10):
            for productid in ware.warehouse1[rownum]:
                for items in productid:
                    if items != '':
                        products.append(items)
            for ids in products:
                refpos = ref[ids]
                dref = Decoder(refpos)
                position = self.b.memory[ids]
                if refpos not in self.b.existingPos:
                    d = Decoder(position)
                    if position[0] == '1':
                        ware.warehouse1[d.Row][d.Y][d.X] = ''
                    elif position[0] == '2':
                        ware.warehouse2[d.Row][d.Y][d.X] = ''
                    elif position[0] == '3':
                        ware.warehouse3[d.Row][d.Y][d.X] = ''
                    elif position[0] == '4':
                        ware.warehouse4[d.Row][d.Y][d.X] = ''
                    elif position[0] == '5':
                        ware.warehouse5[d.Row][d.Y][d.X] = ''
                    self.b.existingPos.remove(position)
                    self.b.memory[ids] = refpos
                    self.b.existingPos.append(refpos)         
                    if refpos[0] == '1':    
                        ware.warehouse1[dref.Row][dref.Y][dref.X] = ids
                    elif refpos[0] == '2':
                        ware.warehouse2[dref.Row][dref.Y][dref.X] = ids
                    elif refpos[0] == '3':
                        ware.warehouse3[dref.Row][dref.Y][dref.X] = ids
                        print(1)
                    elif refpos[0] == '4':
                        ware.warehouse4[dref.Row][dref.Y][dref.X] = ids
                    elif refpos[0] == '5':
                        ware.warehouse5[dref.Row][dref.Y][dref.X] = ids
                else:
                    pass
            products.clear()
            print('Sorting process for warehouse A is complete.')
            self.command()

        elif warenum == '2' and rownum in range(10):
            for productid in ware.warehouse2[rownum]:
                for items in productid:
                    if items != '':
                        products.append(items)
            for ids in products:
                refpos = ref[ids]
                dref = Decoder(refpos)
                position = self.b.memory[ids]
                if refpos not in self.b.existingPos:
                    d = Decoder(position)
                    if position[0] == '1':
                        ware.warehouse1[d.Row][d.Y][d.X] = ''
                    elif position[0] == '2':
                        ware.warehouse2[d.Row][d.Y][d.X] = ''
                    elif position[0] == '3':
                        ware.warehouse3[d.Row][d.Y][d.X] = ''
                    elif position[0] == '4':
                        ware.warehouse4[d.Row][d.Y][d.X] = ''
                    elif position[0] == '5':
                        ware.warehouse5[d.Row][d.Y][d.X] = ''
                    self.b.existingPos.remove(position)
                    self.b.memory[ids] = refpos
                    self.b.existingPos.append(refpos)         
                    if refpos[0] == '1':    
                        ware.warehouse1[dref.Row][dref.Y][dref.X] = ids
                    elif refpos[0] == '2':
                        ware.warehouse2[dref.Row][dref.Y][dref.X] = ids
                    elif refpos[0] == '3':
                        ware.warehouse3[dref.Row][dref.Y][dref.X] = ids
                        print(1)
                    elif refpos[0] == '4':
                        ware.warehouse4[dref.Row][dref.Y][dref.X] = ids
                    elif refpos[0] == '5':
                        ware.warehouse5[dref.Row][dref.Y][dref.X] = ids
                else:
                    pass
            products.clear()
            print('Sorting process for warehouse B is complete.')
            self.command()

        elif warenum == '3' and rownum in range(10):
            for productid in ware.warehouse3[rownum]:
                for items in productid:
                    if items != '':
                        products.append(items)
            for ids in products:
                refpos = ref[ids]
                dref = Decoder(refpos)
                position = self.b.memory[ids]
                if refpos not in self.b.existingPos:
                    d = Decoder(position)
                    if position[0] == '1':
                        ware.warehouse1[d.Row][d.Y][d.X] = ''
                    elif position[0] == '2':
                        ware.warehouse2[d.Row][d.Y][d.X] = ''
                    elif position[0] == '3':
                        ware.warehouse3[d.Row][d.Y][d.X] = ''
                    elif position[0] == '4':
                        ware.warehouse4[d.Row][d.Y][d.X] = ''
                    elif position[0] == '5':
                        ware.warehouse5[d.Row][d.Y][d.X] = ''
                    self.b.existingPos.remove(position)
                    self.b.memory[ids] = refpos
                    self.b.existingPos.append(refpos)         
                    if refpos[0] == '1':    
                        ware.warehouse1[dref.Row][dref.Y][dref.X] = ids
                    elif refpos[0] == '2':
                        ware.warehouse2[dref.Row][dref.Y][dref.X] = ids
                    elif refpos[0] == '3':
                        ware.warehouse3[dref.Row][dref.Y][dref.X] = ids
                        print(1)
                    elif refpos[0] == '4':
                        ware.warehouse4[dref.Row][dref.Y][dref.X] = ids
                    elif refpos[0] == '5':
                        ware.warehouse5[dref.Row][dref.Y][dref.X] = ids
                else:
                    pass
            products.clear()
            print('Sorting process for warehouse C is complete.')
            self.command()

        elif warenum == '4' and rownum in range(8):
            for productid in ware.warehouse4[rownum]:
                for items in productid:
                    if items != '':
                        products.append(items)
            for ids in products:
                refpos = ref[ids]
                dref = Decoder(refpos)
                position = self.b.memory[ids]
                if refpos not in self.b.existingPos:
                    d = Decoder(position)
                    if position[0] == '1':
                        ware.warehouse1[d.Row][d.Y][d.X] = ''
                    elif position[0] == '2':
                        ware.warehouse2[d.Row][d.Y][d.X] = ''
                    elif position[0] == '3':
                        ware.warehouse3[d.Row][d.Y][d.X] = ''
                    elif position[0] == '4':
                        ware.warehouse4[d.Row][d.Y][d.X] = ''
                    elif position[0] == '5':
                        ware.warehouse5[d.Row][d.Y][d.X] = ''
                    self.b.existingPos.remove(position)
                    self.b.memory[ids] = refpos
                    self.b.existingPos.append(refpos)         
                    if refpos[0] == '1':    
                        ware.warehouse1[dref.Row][dref.Y][dref.X] = ids
                    elif refpos[0] == '2':
                        ware.warehouse2[dref.Row][dref.Y][dref.X] = ids
                    elif refpos[0] == '3':
                        ware.warehouse3[dref.Row][dref.Y][dref.X] = ids
                        print(1)
                    elif refpos[0] == '4':
                        ware.warehouse4[dref.Row][dref.Y][dref.X] = ids
                    elif refpos[0] == '5':
                        ware.warehouse5[dref.Row][dref.Y][dref.X] = ids
                else:
                    pass
            products.clear()
            print('Sorting process for warehouse D is complete.')
            self.command()

        elif warenum == '5' and rownum in range(20):
            for productid in ware.warehouse5[rownum]:
                for items in productid:
                    if items != '':
                        products.append(items)
            for ids in products:
                refpos = ref[ids]
                dref = Decoder(refpos)
                position = self.b.memory[ids]
                if refpos not in self.b.existingPos:
                    d = Decoder(position)
                    if position[0] == '1':
                        ware.warehouse1[d.Row][d.Y][d.X] = ''
                    elif position[0] == '2':
                        ware.warehouse2[d.Row][d.Y][d.X] = ''
                    elif position[0] == '3':
                        ware.warehouse3[d.Row][d.Y][d.X] = ''
                    elif position[0] == '4':
                        ware.warehouse4[d.Row][d.Y][d.X] = ''
                    elif position[0] == '5':
                        ware.warehouse5[d.Row][d.Y][d.X] = ''
                    self.b.existingPos.remove(position)
                    self.b.memory[ids] = refpos
                    self.b.existingPos.append(refpos)         
                    if refpos[0] == '1':    
                        ware.warehouse1[dref.Row][dref.Y][dref.X] = ids
                    elif refpos[0] == '2':
                        ware.warehouse2[dref.Row][dref.Y][dref.X] = ids
                    elif refpos[0] == '3':
                        ware.warehouse3[dref.Row][dref.Y][dref.X] = ids
                    elif refpos[0] == '4':
                        ware.warehouse4[dref.Row][dref.Y][dref.X] = ids
                    elif refpos[0] == '5':
                        ware.warehouse5[dref.Row][dref.Y][dref.X] = ids
                else:
                    pass
            products.clear()
            print('Sorting process for warehouse E is complete.')
            self.command()
        else:
            print('That row does not exist')
            self.command()
        
    def RetrieveBelt(self):
        if self.Code == '30000':
            if self.c.size() > 0:
                print('Retrieve a product with id ' + self.c.items[-1] + ' from the belt.')
                del self.b.memory[self.c.items[-1]]
                self.c.retrievebelt()
                print('The belt now has ' + str(self.c.size()) + ' products on the line.')
                
            elif self.c.size() <= 0:
                print('The belt is empty. Cannot retrieve product from the belt.')
            self.command()
        else:
            print('Command is not recognized. Please refer to command help')
            self.command()

    def Output(self):
        if self.Code == '40000':
            self.w.outputwarehouse()
            self.command()
        else:
            print('Command is not recognized')
            self.help()
            self.command()
    
    def Search(self):
        productid = self.Code[1:]
        if  productid not in self.b.memory or productid in self.c.items:
            print('Product not found.')
            self.command()
        elif self.b.memory[productid]:
            position = self.b.memory[productid]
            d = Decoder(position)
            print('Found product at Warehouse:' + str(d.wnum) + ' Row:' + str(d.Row) + ' X:' + str(d.X) + ' Y:' + str(d.Y))
            self.command()
        else:
            print('Product not found.')
            self.command()
    
    def Manual(self):
        ware = self.w
        productid = self.Code[1:5]
        newpos = self.Code[5:]
        d = Decoder(newpos)
        if productid in self.b.memory and newpos not in self.b.existingPos and d.Row in range(20) and d.Y in range(20) and d.X in range(20):
            position = self.b.memory[productid]
            d = Decoder(position)
            if position[0] == '1':
                ware.warehouse1[d.Row][d.Y][d.X] = ''
            elif position[0] == '2':
                ware.warehouse2[d.Row][d.Y][d.X] = ''
            elif position[0] == '3':
                ware.warehouse3[d.Row][d.Y][d.X] = ''
            elif position[0] == '4':
                ware.warehouse4[d.Row][d.Y][d.X] = ''
            elif position[0] == '5':
                ware.warehouse5[d.Row][d.Y][d.X] = ''
            self.b.existingPos.remove(position)
            self.b.memory[productid] = newpos
            d2 = Decoder(newpos)
            if  newpos[0] == '1' and d2.Row in range(5) and d2.Y in range(10) and d2.X in range(10):
                ware.warehouse1[d2.Row][d2.Y][d2.X] = productid
            elif newpos[0] == '2' and d2.Row in range(5) and d2.Y in range(10) and d2.X in range(10):
                ware.warehouse2[d2.Row][d2.Y][d2.X] = productid
            elif newpos[0] == '3' and d2.Row in range(5) and d2.Y in range(10) and d2.X in range(10):
                ware.warehouse3[d2.Row][d2.Y][d2.X] = productid
            elif newpos[0] == '4' and d2.Row in range(7) and d2.Y in range(6) and d2.X in range(6):
                ware.warehouse4[d2.Row][d2.Y][d2.X] = productid
            elif newpos[0] == '5' and d2.Row in range(20) and d2.Y in range(20) and d2.X in range(20):
                ware.warehouse5[d2.Row][d2.Y][d2.X] = productid
            self.b.existingPos.append(newpos)
            print('Move Product ' + productid + ' to Warehouse:' + str(d2.wnum) + ' Row:' + str(d2.Row) + ' Y:' + str(d2.Y) + ' X:' + str(d2.X))
            self.command()
        else:
            print('Slot is occupied. Failed to move')
            self.command()
    
    def help(self):
        print('       0ABCD - Retrive product ABCD.                    // A[A-Y] B[1-5] C[0-9] D[0-9] ')
        print('       1ABCD - Store product ABCD.                      // A[A-Y] B[1-5] C[0-9] D[0-9] ')
        print('       2AB00 - Sort Warehouse A Row B.                  // A[1-5] B[01-20]')
        print('       30000 - Retrieve a product from the belt.')
        print('       40000 - Output information of all houses.')
        print('       5ABCD - Search for product ABCD.                 // A[A-Y] B[1-5] C[0-9] D[0-9]')
        print('9ABCDWRRYYXX - Manually move a product ABCD to WRRYYXX. // A[A-Y] B[1-5] C[0-9] D[0-9] W[1-5] RR[01-20] YY[00-19] XX[00-19]')
        print('    examples - Show examples of each command.')
        self.command()

    def examples(self):
        print('       0a100 = Retrieve product A100.')
        print('       1a100 = Store product A100.')
        print('      210100 = Sort warehouse A at row 1.')
        print('       30000 = Retrieve a product from the belt.')
        print('       40000 = Output warehouse information.')
        print('9a1001010000 = Place product a100 at warehouse A row 1 y=00 x=00.')
        self.command()

    def leave(self):
        return(0)

               
c = Commands()