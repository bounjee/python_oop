"""
OOP: OBJECT ORIENTED PROGRAMMING
    - class / object [0,1]
    - attributes / methods [2,3]
    - encapsulation / abstraction [4,5]
    - inheritance [6]
    - overriding / polymorphism [7,8]
"""

"""
Örnek Proje: 
    Bir adet abstract method ( soyut method -- şemalamaya yarar. ) kullanacağız, ismi Shapes --> Şekillerin ortak 
    özellikleri: Area, Perimeter ve ayrı olarak bir toString methodu kullanılacak.
    2 Adet Child class Yazılacak. Square ve Circle --> Shapes ile aynı methodları kullanacak.
"""
"Class'ımızı abstract yapmak için ABC modülünü yüklüyoruz. ABC = Abstract Base Class"
from abc import ABC, abstractmethod

# Inheritance [6]
class Shapes(ABC): # Shapes class'ımız Super Class ve Abstract Method özelliği taşıyacak.

    @abstractmethod # Area'yı abstractmethod'a çevirdik.
    def Area(self): pass # Abstract Method [5]

    @abstractmethod # Perimeter'i abstractmethod'a çevirdik.
    def Perimeter(self): pass # Abstract Method [5]

    def toString(self): pass # Overriding And Polymorphism [7,8]


class Square(Shapes): # Square Class'ı Shapes Class'ının Child'i.

    def __init__(self,edge):
        self.__edge = edge # Encapsulation kullanarak edge'yi gizli hale getirdik. --> Private Attribute

    # @abstractmethod kullandığımız için Area'yı kullanmak zorundayız.
    def Area(self):
        result = self.__edge * self.__edge
        print("Square Area:",result)

    # @abstractmethod kullandığımız için Area'yı kullanmak zorundayız.
    def Perimeter(self):
        result = self.__edge * 4
        print("Square Perimeter:", result)

    def toString(self): # Overriding, Polymorphism [7,8]
        print("Square Edge:",self.__edge)

class Circle(Shapes): # Circle Class'ı Shapes Class'ının Child'i.

    PI = 3.14  # Constant Variable

    def __init__(self,radius):
        self.__radius = radius

    def Area(self):
        result = self.PI * (self.__radius ** 2)
        print("Circle Area:",result)

    def Perimeter(self):
        result = 2* self.PI * self.__radius
        print("Circle Perimeter:",result)

    def toString(self):
        print("Circle Radius:",self.__radius)

"Circle için: "
print("Circle için: ")
circle = Circle(5)
circle.Area()
circle.Perimeter()
circle.toString()
print()

"Square için: "
print("Square için: ")
circle = Circle(5)
circle.Area()
circle.Perimeter()
circle.toString()

