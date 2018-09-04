class winput:
    def __init__(self , _ID):
        self.command=_ID
    def Scan(self,link):
        if self.command[0] == "0":
            link.Retrieve(link)
        elif self.command[0] == "1":
            link.Store(link)
        elif self.command[0] == "2":
            link.Sort(link)
        elif self.command[0] == "3":
            link.RetrieveConveyor(link)
        elif self.command[0] == "4":
            link.OutputInformation(link)
        elif self.command[0] == "5":
            link.Search(link)
        elif self.command[0] == "9":
            link.Maunual(link)
    def Retrieve(self , link):
        print ("Retrieve")
    def Store(self , link):
        print ("Store")
    def Sort(self , link):
        print ("Sort")
    def RetrieveConveyor(self , link):
        print ("RetrieveConveyor")
    def OutputInformation(self , link):
        print ("OutputInformation")
    def Search(self , link):
        print ("Search")
    def Maunual(self , link):
        print ("Maunual")


link = winput("9A125")
link.Scan(link)
