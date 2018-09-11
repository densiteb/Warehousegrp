class conveyerbelt:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def insert(self,item):
        self.items.insert(0,item)

    def retrievebelt(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

convey = conveyerbelt()
convey.insert('A125')
convey.insert('B115')
convey.insert('C255')
print(convey.items)
print(convey.size())
print(convey.retrievebelt())
print(convey.items)