class Logging:
    DEBUG = 0
    INFO = 1
    RELEASE = 2
    ERROR = 3
    
    LEVEL = DEBUG
    
    def __init__(self, level):
        self.LEVEL = level        

    def log(self, level, text):
        try:
            if self.LEVEL <= level : 
                print(text)
        except:
            pass
            
    def PrintList(self, level, itemsList):
        for item in itemsList:
            log(level, item)
            
    def PrintLine(self, level):
        self.log(level, "#############################################################################\n\n\n")
        
    def Print(self, level, text):
        log(level, text)