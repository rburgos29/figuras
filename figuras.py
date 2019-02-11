class Figura():
    def __init__(self):
        pass
    def get_area():
        pass
    def get_perimetro():
        pass

class Cuadrado(Figura):
    def __init__(self,lado):
        self.lado=lado

    def get_area(self):
        self.area=self.lado**2
        return self.area

    def get_perimetro(self):
        self.perimetro=self.lado*4
        return self.get_perimetro

class Rectangulo (Figura):
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    def get_area(self):
        self.area=self.base*self.altura
        return self.get_area

    def get_perimetro(self):
        self.perimetro=self.base*2 + self.altura*2
        return self.perimetro
