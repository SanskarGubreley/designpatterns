from abc import ABC,abstractmethod

class Basepizza(ABC):
    
    @abstractmethod
    def cost(self):
        pass 


class toppings(Basepizza):
    pass 

class extraCheese(toppings):

    def __init__(self, pizza) -> None:
        self.basepizza = pizza
    
    def cost(self):
        return self.basepizza.cost() + 10


class margherita(Basepizza):

    def cost(self):
        return 100 

p = margherita()
q = extraCheese(p)
print(q.cost())