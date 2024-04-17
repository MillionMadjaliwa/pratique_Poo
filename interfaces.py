from abc import ABC, abstractmethod

class IVehicule(ABC):
    @abstractmethod
    def avancer(self):
        pass

class Voiture(IVehicule):
    def avancer(self):
        return "La voiture avance"

class Velo(IVehicule):
    def avancer(self):
        return "Le vélo avance"

voiture = Voiture()
print(voiture.avancer())  # La voiture avance

velo = Velo()
print(velo.avancer())  
