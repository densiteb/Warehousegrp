class conveyerbelt:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def inserttobelt(self,item):
        self.items.insert(0,item)

    def retrievebelt(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
'''c = conveyerbelt()
c.insert('b')
c.insert('c')
print(c.retrievebelt())'''

