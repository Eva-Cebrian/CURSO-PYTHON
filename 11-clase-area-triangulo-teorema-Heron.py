import math

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        
    def semiperimetro(self):
         return (self.lado1 + self.lado2 + self.lado3)/2
        
        
    def area(self):
        semiperimetro = self.semiperimetro()
        area = math.sqrt(semiperimetro * ((semiperimetro - self.lado1) * (semiperimetro - self.lado2) * (semiperimetro - self.lado3)))
        return area
    
    def __str__(self):
        return f"El area del triangulo con lados {self.lado1}, {self.lado2}, {self.lado3} es {self.area():.2f} y su perímetro es: {self.semiperimetro()*2:.2f}"
    
    
    
triangulo1 = Triangulo(2,5,6)
triangulo2 = Triangulo(13,16,23)

print(triangulo1)
print(triangulo2)