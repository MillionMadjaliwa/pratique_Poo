def create_class(name):
    if name == "Voiture":
        class Voiture:
            def vroom(self):
                return "Vroom!"
        return Voiture
    else:
        class Velo:
            def ding(self):
                return "Ding!"
        return Velo

DynamicClass = create_class("Voiture")
voiture = DynamicClass()
print(voiture.vroom())  # Vroom!

DynamicClass = create_class("Velo")
velo = DynamicClass()
print(velo.ding()) 
