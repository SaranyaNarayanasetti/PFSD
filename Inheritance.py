from Fruit import FruitBasket
class Parent():
    def function1(self):
        print("I am the parent")

class Child(Parent,FruitBasket):
    def function2(self,a):
        print("I am the child")
        print(a**2)
    b=10


y=Child()
y.function1()
y.function2(10)
y.intro()
print(y.b)
