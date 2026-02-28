class Logger:

    def __init__(self):
        self.mapOfLogs = {} 

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in  self.mapOfLogs:
            if timestamp >= 10 +  self.mapOfLogs[message]:
                self.mapOfLogs[message] = timestamp
                return True
            else:
                return False
        else:
            self.mapOfLogs[message] = timestamp
            return True 
        
