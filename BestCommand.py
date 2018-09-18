from Conveyerbelt2 import conveyerbelt
from Mainwarehouse import Warehouse
from robotarm import Barcode
from Decoder import Decoder
from Reference import Referto
from NewWarehouse import generateProduct
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
        #elif self.Code == 'LEAVE':
        #   self.leave()
        elif self.Code == 'EXAMPLES':
            self.examples()
        #elif self.Code == 'FILLTHEFUCKINGWAREHOUSE':
        #   self.__fillthefuckingWarehouse__()
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
        elif Code == '9' and len(self.Code) >= 8 and len(self.Code) <= 11 and self.Code[1] in self.alpha:
            self.Manual()
        else:
            print('Command is not recognized.')
            self.help()
            self.command()

    def Retrieve(self):
        ware = self.w
        productid = self.Code[1:]

        if self.c.size() >= 10:
            print('Belt is full.Cannot retrieve product.')
            self.command()
            
        elif int(self.Code[2]) > 5 or int(self.Code[3]) > 9 or int(self.Code[4]) > 9:
            print('Format invalid.')
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
            print('Moving from Belt to Warehouse 1')
            print('Getting a product id ' + productid + ' in Warehouse 1: row '+ str(int(d.Row) + 1) + ' slot ' + str(d.slotnum))
            print('Moving from Warehouse 1 to Start')
            print('Placing product id ' + productid + ' on the belt. ')
            print('Retrieving Successfully!')
            self.b.w1total -= 1
            self.c.inserttobelt(productid)
            self.command()
        
        elif position[0] == '2':
            ware.warehouse2[d.Row][d.Y][d.X] = ''
            self.b.existingPos.remove(position)
            self.b.memory[productid] = 'On the belt'
            print('Moving from Belt to Warehouse 1')
            print('Moving from Warehouse 1 to Warehouse 2')
            print('Getting a product id ' + productid + ' in Warehouse Warehouse 2: row '+ str(int(d.Row) + 1) + ' slot ' + str(d.slotnum))
            print('Moving from Warehouse 2 to Warehouse 1')
            print('Moving from Warehouse 1 to Start')
            print('Placing product id ' + productid + ' on the belt. ')
            print('Retrieving Successfully!')
            self.b.w2total -= 1
            self.c.inserttobelt(productid)
            self.command()
        
        elif position[0] == '3':
            ware.warehouse3[d.Row][d.Y][d.X] = ''
            self.b.existingPos.remove(position)
            self.b.memory[productid] = 'On the belt'
            print('Moving from Belt to Warehouse 1')
            print('Moving from Warehouse 1 to Warehouse 3')
            print('Getting a product id ' + productid + ' in Warehouse C: row '+ str(int(d.Row) + 1) + ' slot ' + str(d.slotnum))
            print('Moving from Warehouse 3 to Warehouse 1' )
            print('Moving from Warehouse 1 to Start')
            print('Placing product id ' + productid + ' on the belt. ')
            print('Retrieving Successfully!')
            self.b.w3total -= 1
            self.c.inserttobelt(productid)
            self.command()
        
        elif position[0] == '4':
            ware.warehouse4[d.Row][d.Y][d.X] = ''
            self.b.existingPos.remove(position)
            self.b.memory[productid] = 'On the belt'
            print('Moving from Belt to Warehouse 1')
            print('Moving from Warehouse 1 to Warehouse 2')
            print('Moving from Warehouse 2 to Warehouse 4')
            print('Getting a product id ' + productid + ' in Warehouse D: row '+ str(int(d.Row) + 1) + ' slot ' + str(d.slotnum))
            print('Moving from Warehouse 4 to Warehouse 2')
            print('Moving from Warehouse 2 to Warehouse 1')
            print('Moving from Warehouse 1 to Start')
            print('Placing product id ' + productid + ' on the belt. ')
            print('Retrieving Successfully!')
            self.b.w4total -= 1
            self.c.inserttobelt(productid)
            self.command()
        
        elif position[0] == '5':
            ware.warehouse5[d.Row][d.Y][d.X] = ''
            self.b.existingPos.remove(position)
            self.b.memory[productid] = 'On the belt'
            print('Moving from Belt to Warehouse 1')
            print('Moving from Warehouse 1 to Warehouse 2')
            print('Moving from Warehouse 2 to Warehouse 5')
            print('Getting a product id ' + productid + ' in Warehouse 5: row '+ str(int(d.Row) + 1) + ' slot ' + str(d.slotnum))
            print('Moving from Warehouse 5 to Warehouse 2')
            print('Moving from Warehouse 2 to Warehouse 1')
            print('Moving from Warehouse 1 to Start')
            print('Placing product id ' + productid + ' on the belt. ')
            print('Retrieving Successfully!')
            self.b.w5total -= 1
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
            self.b.w1total += 1
            print('Moving from Belt to Warehouse 1')
            print('Storing a product id ' + productid + ' in Warehouse Warehouse 1: row '+ str(int(d.Row) + 1) + ' slot ' + str(d.slotnum))
            print('Moving from Warehouse 1 to Start')
            print('Storing Successfully!')
            self.command()

        elif position[0] == '2' and d.Row in range(5) and d.Y in range(10) and d.X in range(10):
            ware.warehouse2[d.Row][d.Y][d.X] = productid
            self.b.w2total += 1
            print('Moving from Belt to Warehouse 1')
            print('Moving from Warehouse 1 to Warehouse 2')
            print('Storing a product id ' + productid + ' in Warehouse 2: row '+ str(int(d.Row) + 1) + ' slot ' + str(d.slotnum))
            print('Moving from Warehouse 2 to Warehouse 1')
            print('Moving from Warehouse 1 to Start')
            print('Storing Successfully!')
            self.command()

        elif position[0] == '3' and d.Row in range(5) and d.Y in range(10) and d.X in range(10):
            ware.warehouse3[d.Row][d.Y][d.X] = productid
            self.b.w3total += 1
            print('Moving from Belt to Warehouse 1')
            print('Moving from Warehouse 1 to Warehouse 3')
            print('Storing a product id ' + productid + ' in Warehouse 3: row '+ str(int(d.Row) + 1) + ' slot ' + str(d.slotnum))
            print('Moving from Warehouse 3 to Warehouse 1' )
            print('Moving from Warehouse 1 to Start')
            print('Storing Successfully!')
            self.command()

        elif position[0] == '4' and d.Row in range(7) and d.Y in range(6) and d.X in range(6):
            ware.warehouse4[d.Row][d.Y][d.X] = productid
            self.b.w4total += 1
            print('Moving from Belt to Warehouse 1')
            print('Moving from Warehouse 1 to Warehouse 2')
            print('Moving from Warehouse 2 to Warehouse 4')
            print('Storing a product id ' + productid + ' in Warehouse 4: row '+ str(int(d.Row) + 1) + str(d.slotnum) )
            print('Moving from Warehouse 4 to Warehouse 2')
            print('Moving from Warehouse 2 to Warehouse 1')
            print('Moving from Warehouse 1 to Start')
            print('Storing Successfully!')
            self.command()

        elif position[0] == '5' and d.Row in range(20) and d.Y in range(20) and d.X in range(20):
            ware.warehouse5[d.Row][d.Y][d.X] = productid
            self.b.w5total += 1
            print('Moving from Belt to Warehouse 1')
            print('Moving from Warehouse 1 to Warehouse 2')
            print('Moving from Warehouse 2 to Warehouse 5')
            print('Storing a product id ' + productid + ' in Warehouse 5: row '+ str(int(d.Row) + 1) + ' slot ' + str(d.slotnum))
            print('Moving from Warehouse 5 to Warehouse 2')
            print('Moving from Warehouse 2 to Warehouse 1')
            print('Moving from Warehouse 1 to Start')
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
                    try:
                        if refpos not in self.b.existingPos:
                            d = Decoder(position)
                            if position[0] == '1':
                                ware.warehouse1[d.Row][d.Y][d.X] = ''
                                self.b.w1total -= 1
                            elif position[0] == '2':
                                ware.warehouse2[d.Row][d.Y][d.X] = ''
                                self.b.w2total -= 1
                            elif position[0] == '3':
                                ware.warehouse3[d.Row][d.Y][d.X] = ''
                                self.b.w3total -= 1
                            elif position[0] == '4':
                                ware.warehouse4[d.Row][d.Y][d.X] = ''
                                self.b.w4total -= 1
                            elif position[0] == '5':
                                ware.warehouse5[d.Row][d.Y][d.X] = ''
                                self.b.w5total -= 1
                            self.b.existingPos.remove(position)
                            self.b.memory[ids] = refpos
                            self.b.existingPos.append(refpos)         
                            if refpos[0] == '1':    
                                ware.warehouse1[dref.Row][dref.Y][dref.X] = ids
                                self.b.w1total += 1
                            elif refpos[0] == '2':
                                ware.warehouse2[dref.Row][dref.Y][dref.X] = ids
                                self.b.w2total += 1
                            elif refpos[0] == '3':
                                ware.warehouse3[dref.Row][dref.Y][dref.X] = ids
                                self.b.w3total += 1
                           
                            elif refpos[0] == '4':
                                ware.warehouse4[dref.Row][dref.Y][dref.X] = ids
                                self.b.w4total += 1
                            elif refpos[0] == '5':
                                ware.warehouse5[dref.Row][dref.Y][dref.X] = ids
                                self.b.w5total += 1
                    except:
                        pass
            products.clear()
            print('Sorting process for warehouse Warehouse 1 is complete.')
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
                    try:
                        if refpos not in self.b.existingPos:
                            d = Decoder(position)
                            if position[0] == '1':
                                ware.warehouse1[d.Row][d.Y][d.X] = ''
                                self.b.w1total -= 1
                            elif position[0] == '2':
                                ware.warehouse2[d.Row][d.Y][d.X] = ''
                                self.b.w2total -= 1
                            elif position[0] == '3':
                                ware.warehouse3[d.Row][d.Y][d.X] = ''
                                self.b.w3total -= 1
                            elif position[0] == '4':
                                ware.warehouse4[d.Row][d.Y][d.X] = ''
                                self.b.w4total -= 1
                            elif position[0] == '5':
                                ware.warehouse5[d.Row][d.Y][d.X] = ''
                                self.b.w5total -= 1
                            self.b.existingPos.remove(position)
                            self.b.memory[ids] = refpos
                            self.b.existingPos.append(refpos)         
                            if refpos[0] == '1':    
                                ware.warehouse1[dref.Row][dref.Y][dref.X] = ids
                                self.b.w1total += 1
                            elif refpos[0] == '2':
                                ware.warehouse2[dref.Row][dref.Y][dref.X] = ids
                                self.b.w2total += 1
                            elif refpos[0] == '3':
                                ware.warehouse3[dref.Row][dref.Y][dref.X] = ids
                                self.b.w3total += 1
                    
                            elif refpos[0] == '4':
                                ware.warehouse4[dref.Row][dref.Y][dref.X] = ids
                                self.b.w4total += 1
                            elif refpos[0] == '5':
                                ware.warehouse5[dref.Row][dref.Y][dref.X] = ids
                                self.b.w5total += 1
                    except:
                        pass
            products.clear()
            print('Sorting process for warehouse 2 is complete.')
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
                    try:
                        if refpos not in self.b.existingPos:
                            d = Decoder(position)
                            if position[0] == '1':
                                ware.warehouse1[d.Row][d.Y][d.X] = ''
                                self.b.w1total -= 1
                            elif position[0] == '2':
                                ware.warehouse2[d.Row][d.Y][d.X] = ''
                                self.b.w2total -= 1
                            elif position[0] == '3':
                                ware.warehouse3[d.Row][d.Y][d.X] = ''
                                self.b.w3total -= 1
                            elif position[0] == '4':
                                ware.warehouse4[d.Row][d.Y][d.X] = ''
                                self.b.w4total -= 1
                            elif position[0] == '5':
                                ware.warehouse5[d.Row][d.Y][d.X] = ''
                                self.b.w5total -= 1
                            self.b.existingPos.remove(position)
                            self.b.memory[ids] = refpos
                            self.b.existingPos.append(refpos)         
                            if refpos[0] == '1':    
                                ware.warehouse1[dref.Row][dref.Y][dref.X] = ids
                                self.b.w1total += 1
                            elif refpos[0] == '2':
                                ware.warehouse2[dref.Row][dref.Y][dref.X] = ids
                                self.b.w2total += 1
                            elif refpos[0] == '3':
                                ware.warehouse3[dref.Row][dref.Y][dref.X] = ids
                                self.b.w3total += 1
                   
                            elif refpos[0] == '4':
                                ware.warehouse4[dref.Row][dref.Y][dref.X] = ids
                                self.b.w4total += 1
                            elif refpos[0] == '5':
                                ware.warehouse5[dref.Row][dref.Y][dref.X] = ids
                                self.b.w5total += 1
                    except:
                        pass
            products.clear()
            print('Sorting process for warehouse 3 is complete.')
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
                    try:
                        if refpos not in self.b.existingPos:
                            d = Decoder(position)
                            if position[0] == '1':
                                ware.warehouse1[d.Row][d.Y][d.X] = ''
                                self.b.w1total -= 1
                            elif position[0] == '2':
                                ware.warehouse2[d.Row][d.Y][d.X] = ''
                                self.b.w2total -= 1
                            elif position[0] == '3':
                                ware.warehouse3[d.Row][d.Y][d.X] = ''
                                self.b.w3total -= 1
                            elif position[0] == '4':
                                ware.warehouse4[d.Row][d.Y][d.X] = ''
                                self.b.w4total -= 1
                            elif position[0] == '5':
                                ware.warehouse5[d.Row][d.Y][d.X] = ''
                                self.b.w5total -= 1
                            self.b.existingPos.remove(position)
                            self.b.memory[ids] = refpos
                            self.b.existingPos.append(refpos)         
                            if refpos[0] == '1':    
                                ware.warehouse1[dref.Row][dref.Y][dref.X] = ids
                                self.b.w1total += 1
                            elif refpos[0] == '2':
                                ware.warehouse2[dref.Row][dref.Y][dref.X] = ids
                                self.b.w2total += 1
                            elif refpos[0] == '3':
                                ware.warehouse3[dref.Row][dref.Y][dref.X] = ids
                                self.b.w3total += 1
                        
                            elif refpos[0] == '4':
                                ware.warehouse4[dref.Row][dref.Y][dref.X] = ids
                                self.b.w4total += 1
                            elif refpos[0] == '5':
                                ware.warehouse5[dref.Row][dref.Y][dref.X] = ids
                                self.b.w5total += 1
                    except:
                        pass
            products.clear()
            print('Sorting process for warehouse 4 is complete.')
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
                try:
                    if refpos not in self.b.existingPos:
                        d = Decoder(position)
                        if position[0] == '1':
                            ware.warehouse1[d.Row][d.Y][d.X] = ''
                            self.b.w1total -= 1
                        elif position[0] == '2':
                            ware.warehouse2[d.Row][d.Y][d.X] = ''
                            self.b.w2total -= 1
                        elif position[0] == '3':
                            ware.warehouse3[d.Row][d.Y][d.X] = ''
                            self.b.w3total -= 1
                        elif position[0] == '4':
                            ware.warehouse4[d.Row][d.Y][d.X] = ''
                            self.b.w4total -= 1
                        elif position[0] == '5':
                            ware.warehouse5[d.Row][d.Y][d.X] = ''
                            self.b.w5total -= 1
                        self.b.existingPos.remove(position)
                        self.b.memory[ids] = refpos
                        self.b.existingPos.append(refpos)         
                        if refpos[0] == '1':    
                            ware.warehouse1[dref.Row][dref.Y][dref.X] = ids
                            self.b.w1total += 1
                        elif refpos[0] == '2':
                            ware.warehouse2[dref.Row][dref.Y][dref.X] = ids
                            self.b.w2total += 1
                        elif refpos[0] == '3':
                            ware.warehouse3[dref.Row][dref.Y][dref.X] = ids
                            self.b.w3total += 1
                        elif refpos[0] == '4':
                            ware.warehouse4[dref.Row][dref.Y][dref.X] = ids
                            self.b.w4total += 1
                        elif refpos[0] == '5':
                            ware.warehouse5[dref.Row][dref.Y][dref.X] = ids
                            self.b.w5total += 1
                except:
                    pass
            products.clear()
            print('Sorting process for warehouse 5 is complete.')
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
            '''
            self.w.outputwarehouse()
            self.command()
            '''
            productid = self.b.memory.keys()
            rowid = []
            rownum = 1
            print('Warehouse 1')
            print('Number of rows: 5')
            print('Number of total products: ' + str(self.b.w1total))
            for rows in self.w.warehouse1:
                try:
                    for shelfs in rows:
                        for items in shelfs:
                            if items in productid:
                                rowid.append(items)
                    print('Product in row '+ str(rownum) + ': id ' + ' '.join(rowid))
                    rowid.clear()
                except:
                    print('Product in row '+ str(rownum) + ': id -')
                rownum += 1
            rownum = 1

            print('Warehouse 2')
            print('Number of rows: 5')
            print('Number of total products: ' + str(self.b.w2total))
            for rows in self.w.warehouse2:
                try:
                    for shelfs in rows:
                        for items in shelfs:
                            if items in productid:
                                rowid.append(items)
                    print('Product in row '+ str(rownum) + ': id ' + ' '.join(rowid))
                    rowid.clear()
                except:
                    print('Product in row '+ str(rownum) + ': id -')
                rownum += 1
            rownum = 1
            print('Warehouse 3')
            print('Number of rows: 5')
            print('Number of total products: ' + str(self.b.w3total))
            for rows in self.w.warehouse3:
                try:
                    for shelfs in rows:
                        for items in shelfs:
                            if items in productid:
                                rowid.append(items)
                    print('Product in row '+ str(rownum) + ': id ' + ' '.join(rowid))
                    rowid.clear()
                except:
                    print('Product in row '+ str(rownum) + ': id -')
                rownum += 1
            rownum = 1
            print('Warehouse 4')
            print('Number of rows: 7')
            print('Number of total products: ' + str(self.b.w4total))
            for rows in self.w.warehouse4:
                try:
                    for shelfs in rows:
                        for items in shelfs:
                            if items in productid:
                                rowid.append(items)
                    print('Product in row '+ str(rownum) + ': id ' + ' '.join(rowid))
                    rowid.clear()
                except:
                    print('Product in row '+ str(rownum) + ': id -')
                rownum += 1
            rownum = 1
            print('Warehouse 5')
            print('Number of rows: 20')
            print('Number of total products: ' + str(self.b.w5total))
            for rows in self.w.warehouse5:
                try:
                    for shelfs in rows:
                        for items in shelfs:
                            if items in productid:
                                rowid.append(items)
                    print('Product in row '+ str(rownum) + ': id ' + ' '.join(rowid))
                    rowid.clear()
                except:
                    print('Product in row '+ str(rownum) + ': id -')
                rownum += 1
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
        elif productid in self.b.memory:
            try:
                position = self.b.memory[productid]
                d = Decoder(position)
                print('Found product at Warehouse:' + str(d.wnum) + ' Row:' + str(int(d.Row) + 1) + ' Slot:' + str(d.slotnum))
                self.command()
            except:
                print('Oops something went wrong!')
                self.command()
        else:
            print('Product not found.')
            self.command()
    
    def Manual(self):
        ware = self.w
        productid = self.Code[1:5]
        newpos = self.Code[5:]
        try:
            position = self.b.memory[productid]
            d2 = Decoder(newpos + '00000')
            d = Decoder(position)
            if d2.barcode in self.b.existingPos:
                print('Slot is occupied. Failed to move')
                self.command()
                
            if productid in self.b.memory and d2.Row in range(20) and d2.Y in range(20) and d2.X in range(20):
                try: 
                    if position[0] == '1' and d.Row in range(5) and d.Y in range(10) and d.X in range(10):
                        self.b.w1total -= 1
                        ware.warehouse1[d.Row][d.Y][d.X] = ''
                        self.b.existingPos.remove(position)
                        self.b.memory[productid] = d2.barcode
                    elif position[0] == '2' and d.Row in range(5) and d.Y in range(10) and d.X in range(10):
                        self.b.w2total -= 1
                        ware.warehouse2[d.Row][d.Y][d.X] = ''
                        self.b.existingPos.remove(position)
                        self.b.memory[productid] = d2.barcode
                    elif position[0] == '3' and d.Row in range(5) and d.Y in range(10) and d.X in range(10):
                        self.b.w3total -= 1
                        ware.warehouse3[d.Row][d.Y][d.X] = ''
                        self.b.existingPos.remove(position)
                        self.b.memory[productid] = d2.barcode
                    elif position[0] == '4' and d.Row in range(7) and d.Y in range(6) and d.X in range(6):
                        self.b.w4total -= 1
                        ware.warehouse4[d.Row][d.Y][d.X] = ''
                        self.b.existingPos.remove(position)
                        self.b.memory[productid] = d2.barcode
                    elif position[0] == '5' and d.Row in range(20) and d.Y in range(20) and d.X in range(20):
                        self.b.w5total -= 1
                        ware.warehouse5[d.Row][d.Y][d.X] = ''
                        self.b.existingPos.remove(position)
                        self.b.memory[productid] = d2.barcode
                    
        
                    if  newpos[0] == '1' and d2.Row in range(5) and d2.Y in range(10) and d2.X in range(10):
                        self.b.w1total += 1
                        ware.warehouse1[d2.Row][d2.Y][d2.X] = productid
                        self.b.existingPos.append(d2.barcode)
                        print('Move Product ' + productid + ' to Warehouse:' + str(d2.wnum) + ' Row:' + str(int(d2.Row) + 1) + ' Slot:' + str(d2.slotnum))
                        self.command()
                    elif newpos[0] == '2' and d2.Row in range(5) and d2.Y in range(10) and d2.X in range(10):
                        self.b.w2total += 1
                        ware.warehouse2[d2.Row][d2.Y][d2.X] = productid
                        self.b.existingPos.append(d2.barcode)
                        print('Move Product ' + productid + ' to Warehouse:' + str(d2.wnum) + ' Row:' + str(int(d2.Row) + 1) + ' Slot:' + str(d2.slotnum))
                        self.command()
                    elif newpos[0] == '3' and d2.Row in range(5) and d2.Y in range(10) and d2.X in range(10):
                        self.b.w3total += 1
                        ware.warehouse3[d2.Row][d2.Y][d2.X] = productid
                        self.b.existingPos.append(d2.barcode)
                        print('Move Product ' + productid + ' to Warehouse:' + str(d2.wnum) + ' Row:' + str(int(d2.Row) + 1) + ' Slot:' + str(d2.slotnum))
                        self.command()
                    elif newpos[0] == '4' and d2.Row in range(7) and d2.Y in range(6) and d2.X in range(6):
                        self.b.w4total += 1
                        ware.warehouse4[d2.Row][d2.Y][d2.X] = productid
                        self.b.existingPos.append(d2.barcode)
                        print('Move Product ' + productid + ' to Warehouse:' + str(d2.wnum) + ' Row:' + str(int(d2.Row) + 1) + ' Slot:' + str(d2.slotnum))
                        self.command()
                    elif newpos[0] == '5' and d2.Row in range(20) and d2.Y in range(20) and d2.X in range(20):
                        self.b.w5total += 1
                        ware.warehouse5[d2.Row][d2.Y][d2.X] = productid
                        self.b.existingPos.append(d2.barcode)
                        print('Move Product ' + productid + ' to Warehouse:' + str(d2.wnum) + ' Row:' + str(int(d2.Row) + 1) + ' Slot:' + str(d2.slotnum))
                        self.command()
                    else:
                        print('Slot does not exist.')
                        self.command()
                except:
                    print('Oops something went wrong!')
                    self.command()
            else:
                print('Oops something went wrong!')
                self.command()
        except:
            print('Oops something went wrong!')
            self.command()
    
    def help(self):
        print('    0ABCD - Retrive product ABCD.                    // A[A-Y] B[1-5] C[0-9] D[0-9] ')
        print('    1ABCD - Store product ABCD.                      // A[A-Y] B[1-5] C[0-9] D[0-9] ')
        print('    2AB00 - Sort Warehouse A Row B.                  // A[1-5] B[01-20]')
        print('    30000 - Retrieve a product from the belt.')
        print('    40000 - Output information of all houses.')
        print('    5ABCD - Search for product ABCD.                 // A[A-Y] B[1-5] C[0-9] D[0-9]')
        print( '9ABCDEFG - Manually move a product ABCD to EFGH. // A[A-Y] B[1-5] C[0-9] D[0-9] E[1-5] F[01-20] G[1-400]')
        print(' examples - Show examples of each command.')
        self.command()

    def examples(self):
        print('      0a100 = Retrieve product A100.')
        print('      1a100 = Store product A100.')
        print('     210100 = Sort warehouse 1 at row 1.')
        print('      30000 = Retrieve a product from the belt.')
        print('      40000 = Output warehouse information.')
        print('9a100520400 = Place product a100 at warehouse 5 row 20 slot number 400.')
        self.command()
'''
    def __fillthefuckingWarehouse__(self):
        ware = self.w
        for productid in generateProduct():
            try:
                if productid in self.b.memory:
                    print('Product already exists.Cannot store the product.')

                self.b.ConvertProductID(productid)

                if productid not in self.b.memory:
                    print('Slot is occupied.Cannot store the product.')
                position = self.b.memory[productid]
                d = Decoder(position)

                if position[0] == '1' and d.Row in range(5) and d.Y in range(10) and d.X in range(10):
                    ware.warehouse1[d.Row][d.Y][d.X] = productid
                    self.b.w1total += 1
                    print('Moving from Belt to A')
                    print('Storing a product id ' + productid + ' in Warehouse A: row '+ str(int(d.Row)) + ' slot ' + str(d.X))
                    print('Moving from A to Start')
                    print('Storing Successfully!')

                elif position[0] == '2' and d.Row in range(5) and d.Y in range(10) and d.X in range(10):
                    ware.warehouse2[d.Row][d.Y][d.X] = productid
                    self.b.w2total += 1
                    print('Moving from Belt to A')
                    print('Moving from A to B')
                    print('Storing a product id ' + productid + ' in Warehouse B: row '+ str(int(d.Row)) + ' slot ' + str(d.X))
                    print('Moving from B to A')
                    print('Moving from A to Start')
                    print('Storing Successfully!')

                elif position[0] == '3' and d.Row in range(5) and d.Y in range(10) and d.X in range(10):
                    ware.warehouse3[d.Row][d.Y][d.X] = productid
                    self.b.w3total += 1
                    print('Moving from Belt to A')
                    print('Moving from A to C')
                    print('Storing a product id ' + productid + ' in Warehouse C: row '+ str(int(d.Row)) + ' slot ' + str(d.X))
                    print('Moving from C to A' )
                    print('Moving from A to Start')
                    print('Storing Successfully!')

                elif position[0] == '4' and d.Row in range(7) and d.Y in range(6) and d.X in range(6):
                    ware.warehouse4[d.Row][d.Y][d.X] = productid
                    self.b.w4total += 1
                    print('Moving from Belt to A')
                    print('Moving from A to B')
                    print('Moving from B to D')
                    print('Storing a product id ' + productid + ' in Warehouse D: row '+ str(int(d.Row)) + ' slot ' + str(d.X))
                    print('Moving from D to B')
                    print('Moving from B to A')
                    print('Moving from A to Start')
                    print('Storing Successfully!')

                elif position[0] == '5' and d.Row in range(20) and d.Y in range(20) and d.X in range(20):
                    ware.warehouse5[d.Row][d.Y][d.X] = productid
                    self.b.w5total += 1
                    print('Moving from Belt to A')
                    print('Moving from A to B')
                    print('Moving from B to E')
                    print('Storing a product id ' + productid + ' in Warehouse E: row '+ str(int(d.Row)) + ' slot ' + str(d.X))
                    print('Moving from E to B')
                    print('Moving from B to A')
                    print('Moving from A to Start')
                    print('Storing Successfully!')
            except:
                pass
        self.command()
    def leave(self):
        return(0)
        '''

c = Commands()