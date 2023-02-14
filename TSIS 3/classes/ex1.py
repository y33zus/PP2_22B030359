class Strings:
    def __init__(self):
        self.string=""
    def getString(self):
        self.string = input()
        
    def printString(self):
        print(self.string.upper())
obj = Strings()
obj.getString()
obj.printString()