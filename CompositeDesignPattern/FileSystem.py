from abc import ABC,abstractclassmethod

class FileSystem(ABC):

    @abstractclassmethod
    def ls(self):
        pass 

