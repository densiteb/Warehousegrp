import string
alpha = string.ascii_uppercase.replace('Z','')
alphab = ''
wnum = 0
firstnum = 0
secondnum = 0
productid = []
convertedid = []
hashindex = []
for first in alpha:
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
                productid.append(first + str(wnum) + str(firstnum) + str(secondnum))
                convertedid.append(str(ord(first)) + str(wnum) + str(firstnum) + str(secondnum))
            secondnum = -1
        firstnum = -1
 
 #-65%19 hash function

    