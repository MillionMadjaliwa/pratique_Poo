from abc import ABC, abstractmethod

class Animal(ABC):
    def son(self):
        pass

class Chien(Animal):
    def son(self):
        return "Woof!"

class Chat(Animal):
    def son(self):
        return "Meow!"

# Vous ne pouvez pas créer une instance de Animal car c'est une classe abstraite
#animal = Animal()


# Mais vous pouvez créer des instances de ses sous-classes
chien = Chien()
print(chien.son())  # Woof!

chat = Chat()
print(chat.son())  
