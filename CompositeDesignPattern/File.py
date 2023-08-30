from FileSystem import *

class File(FileSystem):

    def __init__(self,fileName) -> None:
        self.fileName = fileName

    def ls(self):
        print("file name is", self.fileName)

