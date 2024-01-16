from time import sleep
from exo1 import Robot

class Human():
    __sexe = None
    def __init__(self, sexe):
        if sexe == 'M' or sexe == 'F' or sexe == 'H':
            self.__sexe = sexe
            self.__eaten_aliments = []
            self.__count_eaten_aliments = 0

    def eat(self, aliments):
        if type(aliments) is str:
            self.__eaten_aliments.append(aliments)
            self.__count_eaten_aliments += 1
            print("Je mange {} ({} {})".format(aliments, self.__count_eaten_aliments, "aliments mangés" if self.__count_eaten_aliments > 1 else "aliment mangé"))
        elif type(aliments) is list and type(aliments[0]) is str:
            self.__eaten_aliments.extend(aliments)
            for aliment in aliments:
                self.__count_eaten_aliments += 1
                print("Je mange {} ({} {})".format(aliment, self.__count_eaten_aliments,  "aliments mangés" if self.__count_eaten_aliments > 1 else "aliment mangé"))
        
    def digest(self):
        for i in range(self.__count_eaten_aliments):
            print("Digestion en cours ({}/{})".format(i+1, self.__count_eaten_aliments), flush=True, end='\r')
            sleep(1)
        print()
        self.__eaten_aliments.clear()
        self.__count_eaten_aliments = 0

    def status(self):
        print("Sexe : {}\nAliments mangés : {}".format(self.__sexe, self.__eaten_aliments))

    @property
    def sexe(self):
        return self.__sexe
    @sexe.setter
    def sexe(self, new_sexe):
        if new_sexe == 'M' or new_sexe == 'F' or new_sexe == 'H':
            self.__sexe = new_sexe
    
    @property
    def count_eaten_aliments(self):
        return self.__count_eaten_aliments
    
    @property
    def eaten_aliments(self):
        return self.__eaten_aliments


class Cyborg(Robot, Human):   
    def __init__(self, name, sexe):   
        Robot.__init__(self, name)
        Human.__init__(self, sexe)

    def listen_people(self):
        print('Conversation entendue à 2km :\n"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Magna eget est lorem ipsum dolor sit amet consectetur. Tortor condimentum lacinia quis vel eros donec ac. Auctor urna nunc id cursus metus aliquam eleifend mi. Parturient montes nascetur ridiculus mus mauris."')

    def status(self):
        Robot.status(self)
        Human.status(self)

if __name__ == "__main__":
    cyborg = Cyborg('Deux Ex Machina', 'M')

    print(cyborg.name, 'sexe', cyborg.sexe)
    print('Charging battery...')
    #cyborg.charge()
    cyborg.status()
    cyborg.eat('banana')
    cyborg.eat(['coca', 'chips'])
    cyborg.digest()
    cyborg.listen_people()