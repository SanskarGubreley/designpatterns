from logProcessor import LogProcessor

class DebugLogProcessor(LogProcessor):

    def __init__(self, nextLogProcessor) -> None:
        super().__init__(nextLogProcessor)

    def log(self,logLevel,message):
        if logLevel == self.DEBUG:
            print(logLevel, message)
        else:
            super().log(logLevel,message)
            