from abc import ABCMeta, abstractmethod

# You can use classes below or create your own 👍️

class UnmannedVehicle(metaclass=ABCMeta):
    @abstractmethod
    def do_mission(self):
        pass

class GroundVehicle(metaclass=ABCMeta):
    @abstractmethod
    def ride(self):
        pass

class AerialVehicle(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass

class UnderwaterVehicle(metaclass=ABCMeta):
    @abstractmethod
    def navigate_underwater(self):
        pass

class UUV(UnmannedVehicle, UnderwaterVehicle):
    def navigate_underwater(self):
        print("Je navigue sous l'eau !")

    def do_mission(self):
        print("J'effectue ma mission sous l'eau !")

class UAV(UnmannedVehicle, AerialVehicle):
    def fly(self):
        print("Je vole !")
    
    def do_mission(self):
        print("J'effectue ma mission dans le ciel !")

class UGV(UnmannedVehicle, GroundVehicle):
    def ride(self):
        print("Je roule vite !")

    def do_mission(self):
        print("J'effectue ma mission sur terre !")


if __name__ == '__main__':
    uav = UAV()
    uav.fly()
    uav.do_mission()
    

    ugv = UGV()
    ugv.ride()
    ugv.do_mission()
    

    uuv = UUV()
    uuv.navigate_underwater()
    uuv.do_mission()
    