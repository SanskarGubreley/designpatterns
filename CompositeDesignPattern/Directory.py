from FileSystem import * 

class Directory(FileSystem):

    def __init__(self,name) -> None:
        self.directoryName = name 
        self.objList = list()

    def add(self,fileSystemObj):
        self.objList.append(fileSystemObj)

    def ls(self):
        print("DirectoryName ",self.directoryName)
        for obj in self.objList:
            obj.ls()