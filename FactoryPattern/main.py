from abc import ABC,abstractmethod
class shapeFactory:

    def getShape(self,input):

        if input == "circle":
            return Circle()
        elif input == 'rectangle':
            return Rectangle()
        else: 
            return None  
    
class shape(ABC):
    def draw(self): pass

class Circle(shape):
    def draw(self):
        print("circle")

class Rectangle(shape):
    def draw(self):
        print("rectangle")

if __name__ == "__main__":
    obj = shapeFactory()
    shapeObj = obj.getShape("circle")
    shapeObj.draw()