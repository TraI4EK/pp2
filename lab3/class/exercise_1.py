class InOut:
    def getstring(self):
        self.string = input()
    
    def printString(self):
        print(self.string.upper())

result = InOut()

result.getstring() 
result.printString() 