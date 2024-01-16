from time import sleep
from exo1 import Robot

class Human():
    def __init__(self, sexe):
        self.__sexe = sexe
        self.__aliments_manges = []
        self.__nbre_aliments_manges = 0

    def eat(self, aliments):
        if type(aliments) is str:
            self.__nbre_aliments_manges += 1
            print("Je mange {} ({} aliments mangés)".format(aliments, self.__nbre_aliments_manges))
        else:
            for aliment in aliments:
                self.__nbre_aliments_manges += 1
                print("Je mange {} ({} aliments mangés)".format(aliment, self.__nbre_aliments_manges))
        
        self.__aliments_manges.append(aliments)

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
        self.__sexe = new_sexe


class Cyborg(Robot, Human):   
    def __init__(self, name, sexe):   
        Robot.__init__(self, name)
        Human.__init__(self, sexe)

    def truc_fun():
        pass

if __name__ == "__main__":
    cyborg = Cyborg('Deux Ex Machina', 'M')

    print(cyborg.name, 'sexe', cyborg.sexe)
    print('Charging battery...')
    cyborg.charge()
    cyborg.status()
    cyborg.eat('banana')
    cyborg.eat(['coca', 'chips'])
    cyborg.digest()
    # cyborg.truc_fun()