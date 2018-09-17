import string
def generateProduct():
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
            for location in range(10):
                firstnum += 1
                for locate in range(10):
                    secondnum += 1
                    productid.append(str(first) + str(wnum) + str(firstnum) + str(secondnum))
                    #convertedid.append(str(ord(first)) + str(wnum) + str(firstnum) + str(secondnum)
                    #first = ord(str(first)) % 5
                    #if ord(str(first)) >= ord('J'):
                        #hashindex.append(str(first) + str(wnum) + str(firstnum) + str(secondnum))
                    #print(str(first) + str(wnum) + str(firstnum) + str(secondnum))
                secondnum = -1
            firstnum = -1
    return productid



'''
ware1 = 0
ware2 = 0
ware3 = 0
ware4 = 0
ware5 = 0
notallocated = 0
for ids in hashindex:
    if ids[0] == '0':
        ware1 += 1
    elif ids[0] == '1':
        ware2 += 1
    elif ids[0] == '2':
        ware3 += 1
    elif ids[0] == '3':
        ware4 += 1
    elif ids[0] == '4':
        ware5 += 1
    else:
        notallocated += 1
#print(ware1,ware2,ware3,ware4,ware5,notallocated)    
print(len(hashindex))'''
    