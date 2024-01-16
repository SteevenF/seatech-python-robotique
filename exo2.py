from time import sleep
from exo1 import Robot

class Human():
    __sexe = None
    def __init__(self, sexe):
        if sexe == 'M' or sexe == 'F' or sexe == 'H':
            self.__sexe = sexe
            self.__aliments_manges = []
            self.__nbre_aliments_manges = 0

    def eat(self, aliments):
        if type(aliments) is str:
            self.__aliments_manges.append(aliments)
            self.__nbre_aliments_manges += 1
            print("Je mange {} ({} aliments mangés)".format(aliments, self.__nbre_aliments_manges))
        elif type(aliments) is list and type(aliments[0]) is str:
            self.__aliments_manges.extend(aliments)
            for aliment in aliments:
                self.__nbre_aliments_manges += 1
                print("Je mange {} ({} aliments mangés)".format(aliment, self.__nbre_aliments_manges))
        
    def digest(self):
        for i in range(self.__nbre_aliments_manges):
            print("Digestion en cours ({}/{})".format(i+1, self.__nbre_aliments_manges), flush=True, end='\r')
            sleep(1)
        print()

    @property
    def sexe(self):
        return self.__sexe
    @sexe.setter
    def sexe(self, new_sexe):
        if new_sexe == 'M' or new_sexe == 'F' or new_sexe == 'H':
            self.__sexe = new_sexe


class Cyborg(Robot, Human):   
    def __init__(self, name, sexe):   
        Robot.__init__(self, name)
        Human.__init__(self, sexe)

    def listen_people(self):
        print('Conversation entendue à 2km :\n"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Magna eget est lorem ipsum dolor sit amet consectetur. Tortor condimentum lacinia quis vel eros donec ac. Auctor urna nunc id cursus metus aliquam eleifend mi. Parturient montes nascetur ridiculus mus mauris."')

if __name__ == "__main__":
    cyborg = Cyborg('Deux Ex Machina', 'M')

    print(cyborg.name, 'sexe', cyborg.sexe)
    print('Charging battery...')
    cyborg.charge()
    cyborg.status()
    cyborg.eat('banana')
    cyborg.eat(['coca', 'chips'])
    cyborg.digest()
    cyborg.listen_people()