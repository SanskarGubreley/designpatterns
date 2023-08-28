
class LogProcessor:

    def __init__(self,nextLogProcessor) -> None:
        self.INFO = 1
        self.DEBUG = 2
        self.ERROR = 3
        self.nextLogProcessor = nextLogProcessor

    def log(self,logLevel,message):
        if logLevel != None:
            self.nextLogProcessor.log(logLevel,message)


