def store(x) :
    i = 1 
    yz = 100
    countw4 = 0
    '''product_id  = command[1:5]'''
    if '''product_id'''[0] in "ABCDEFGHI":
        if '''warehouse1''':
            for i in range(self.row):
                for j in range(self.yd):
                    for k in range(self.xd):
                            if yz == int('''product_id'''[2:5]):
                                if "A_I"+str(yz) in '''warehouse1''' and  '''warehouse1'''.get("ABC"+str(yz)) == "none" and ("A" + str(yz) not in '''warehouse1'''or"B" + str(yz) not in '''warehouse1'''or"C" + str(yz) not in '''warehouse1'''):
                                    '''warehouse1'''["ABC"+str(yz)] = '''warehouse'''.pop('''product_id''')
                                    '''warehouse1'''['''product_id'''] = "ROW : " + str(i) + ", " + "X : " + str(k) + ", " + "Y : " + str(j)
                                    yz = 100
                                    break
                                elif "W1S"+str(yz) in '''warehouse4''' and'''warehouse4'''.get("W1S"+str(yz)) == "none" and("A" + str(yz) in '''warehouse1'''or"B" + str(yz) in '''warehouse1'''or"C" + str(yz) in '''warehouse1'''):
                                    '''warehouse4'''["W1S"+str(yz)] = '''warehouse'''.pop('''product_id''')
                                    '''warehouse4'''['''product_id'''] = "ROW : " + str(i) + ", " + "X : " + str(k) + ", " + "Y : " + str(j)
                                    yz = 100
                                    break
                            yz += 1
        elif '''warehouse2''':
            for i in range(self.row):
                for j in range(self.yd):
                    for k in range(self.xd):
                            if yz == int('''product_id'''[2:5]):
                                if "A_I"+str(yz) in '''warehouse2''' and  '''warehouse2'''.get("A_I"+str(yz)) == "none" and ("D" + str(yz) not in '''warehouse2'''or"E" + str(yz) not in '''warehouse1'''or"F" + str(yz) not in '''warehouse2'''):
                                    '''warehouse2'''["A_I"+str(yz)] = '''warehouse'''.pop('''product_id''')
                                    '''warehouse2'''['''product_id'''] = "ROW : " + str(i) + ", " + "X : " + str(k) + ", " + "Y : " + str(j)
                                    yz = 100
                                    break
                                elif "W2S"+str(yz) in '''warehouse4''' and'''warehouse4'''.get("W2S"+str(yz)) == "none" and("D" + str(yz) in '''warehouse2'''or"E" + str(yz) in '''warehouse2'''or"F" + str(yz) in '''warehouse2'''):
                                    '''warehouse4'''["W2S"+str(yz)] = '''warehouse'''.pop('''product_id''')
                                    '''warehouse4'''['''product_id'''] = "ROW : " + str(i) + ", " + "X : " + str(k) + ", " + "Y : " + str(j)
                                    yz = 100
                                    break
                            yz += 1
        elif '''warehouse3''':
            for i in range(self.row):
                for j in range(self.yd):
                    for k in range(self.xd):
                            if yz == int('''product_id'''[2:5]):
                                if "A_I"+str(yz) in '''warehouse3''' and  '''warehouse3'''.get("A_I"+str(yz)) == "none" and ("G" + str(yz) not in '''warehouse3'''or"H" + str(yz) not in '''warehouse3'''or"I" + str(yz) not in '''warehouse3'''):
                                    '''warehouse3'''["A_I"+str(yz)] = '''warehouse3'''.pop('''product_id''')
                                    '''warehouse3'''['''product_id'''] = "ROW : " + str(i) + ", " + "X : " + str(k) + ", " + "Y : " + str(j)
                                    yz = 100
                                    break
                                elif "W3S"+str(yz) in '''warehouse4''' and'''warehouse4'''.get("W3S"+str(yz)) == "none" and("D" + str(yz) in '''warehouse3'''or"E" + str(yz) in '''warehouse3'''or"F" + str(yz) in '''warehouse3'''):
                                    '''warehouse4'''["W3S"+str(yz)] = '''warehouse'''.pop('''product_id''')
                                    '''warehouse4'''['''product_id'''] = "ROW : " + str(i) + ", " + "X : " + str(k) + ", " + "Y : " + str(j)
                                    yz = 100
                                    break
                            yz += 1
                            
        elif '''warehouse5''':
            for i in range(self.row):
                for j in range(self.yd):
                    for k in range(self.xd):
                        if yz == int('''product_id'''[2:5]):
                            '''warehouse5'''['''product'''] = "ROW : " + str(i) + ", " + "X : " + str(k) + ", " + "Y : " + str(j)
            

                            
