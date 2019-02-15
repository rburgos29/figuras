class Fraccion():
    def __init__(self,numero,num):
        self.numero = numero
        self.num = num

    def sumar(self):
        return self.numero + self.num

    def restar(self):
        return self.numero - self.num

    def multiplicar(self):
        return self.numero * self.num

    def dividir(self):
        return self.numero / self.num

y = Fraccion(8,9)

suma = y.sumar()
resta = y.restar()
mult = y.multiplicar()
div = y.dividir()

print("La suma es:", suma)
print(" la resta:",resta)
print("la multiplicacion:",mult)
print("la division:",div)
