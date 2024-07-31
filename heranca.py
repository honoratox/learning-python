
class Animal (object): # Classe pai
    pass

class Vertebrate (Animal): # Classe filha de Animal
    pass

class Fish (Vertebrate): # Classe filha de Vertebrate
    def speak(self):
        return "Blub"

class ClownFish (Fish): # Classe filha de Fish
    pass

class TangFish (Fish): # Classe filha de Fish
    pass

dory = TangFish()
dory.speak() # Retorna "Blub"

nemo = ClownFish()
nemo.speak() # Retorna "Blub"
