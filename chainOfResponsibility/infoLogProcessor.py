from logProcessor import *

class InfoLogProcessor(LogProcessor):

    def __init__(self, nextLogProcessor) -> None:
        super().__init__(nextLogProcessor)

    def log(self,logLevel,message):
        if logLevel == self.INFO:
            print(logLevel, message)
        else:
            super().log(logLevel,message)
            