from pandas import pandas
w, h = 300, 200
blockSize = 20
totalList = []

for xStart in xrange(0, w, blockSize):
    xEnd = min(xStart+blockSize, w)
    for yStart in range(0, h, blockSize):
        yEnd = min(yStart+blockSize, h)
        partCoords = [(x,y) for x in xrange(xStart, xEnd) for y in xrange(yStart, yEnd)]
        totalList.append(partCoords)

print(pandas.DataFrame(totalList))
        

        
        
        
        