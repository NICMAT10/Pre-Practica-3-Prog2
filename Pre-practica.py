class Vehiculo:
    def __init__(self,marca,ruedas,color,enMarcha = False):
        self.marca = marca
        self.ruedas = ruedas
        self.color = color
        self.enMarcha = enMarcha
        
    def arrancar (self):
        self.enMarcha = True
        
    def tipoVehiculo (self):
        if(self.ruedas == 4):
            print("Tipo de vehiculo: Automovil")
        else:
            print("Tipo de vehiculo: Moto")
            
    def mostrar(self):
        print(self.marca)
        print(self.ruedas)
        print(self.color)
        print(self.enMarcha)
        
        
Duster = Vehiculo('Renault', 4, 'Beige', True,)
Wave = Vehiculo('Honda', 2, 'Rojo')
Duster.tipoVehiculo()
Wave.tipoVehiculo()
Duster.mostrar()
        