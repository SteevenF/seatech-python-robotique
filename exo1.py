from time import sleep
from time import time

class Robot():
    __name = "<unnamed>"
    __states = ['shutown', 'running'] 
    
    """
      Give your best code here ( •̀ ω •́ )✧
    """
    def __init__(self, name):
        self.__name = name
        self.__power = False
        self.__current_speed = 0
        self.__battery_level = 0
    
    def allumer(self):
        self.__power = True
    def eteindre(self):
        self.__power = False
    
    def charger(self):
        barre = ""
        print("Niveau de batterie de {} : {{{:100s}}} {}%".format(self.__name, barre, self.__battery_level), flush=True, end='\r')
        while self.__battery_level < 100:
            self.__battery_level += 1
            barre += '#'
            print("Niveau de batterie de {} : {{{:100s}}} {}%".format(self.__name, barre, self.__battery_level), flush=True, end='\r')
            sleep(0.1)
        print()
            
    
    def arret_immediat(self):
        self.__current_speed = 0

    @property
    def vitesse(self):
        return self.__current_speed
    @vitesse.setter
    def vitesse(self, speed):
        self.__current_speed = speed
    
    @property
    def name(self):
        return self.__name
    
    def get_state(self):
        print("Etat : {}\nNiveau de batterie : {}%\nVitesse : {}"\
              .format(self.__states[1] if self.__power else self.__states[0], self.__battery_level, self.__current_speed))

if __name__ == "__main__":
    r = Robot("Le nom")
    r.charger()
    r.get_state()
    r.allumer()
    r.get_state()
