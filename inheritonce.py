""" Parent Class"""
class Animal:
    livingthing=True

    def eat():
      print("eating")
    def sleep():
        print("sleeping")
""" Child Class"""

class goat (Animal):   
    
    def grass():
        print("Its eating gross")
    def herb():
        print("It is herbivorus")
    def sleep():
        print(("Don't sleep you are 820Rs kg"))
    print(goat.livingthing)
    print(Animal.livingthing)
goat.grass()
goat.herb()
goat.eat()
goat.sleep()
Animal.eat()
Animal.sleep()
Animal.herb()

"""Part-2 Calling with the help of an object"""
class Animal:
    livingthing=True

def eat(self):
    print("eating")
    
def sleep(self):
    print("sleep") 
"""child class"""
class goat(Animal):
    def grass(self):
        print("Its eating grass") 
        
    def herb(self):
            print("It is herbivorus")
            def sleep(self):
                print("Don't sleep you are 710Rs kg")
a=Animal()
print(a.livingthing)
a.eat()
a.sleep()

g=goat()
g.grass()
g.herb()
g.sleep()
print(g.livingthing)
g.eat()