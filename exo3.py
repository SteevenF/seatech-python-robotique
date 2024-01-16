from abc import ABCMeta, abstractmethod

# You can use classes below or create your own 👍️

class UnmannedVehicle(metaclass=ABCMeta):
    """ 
        An autonomous vehicle have to do his mission automatically.
        This mission can be configured by an operator.
    """
    @abstractmethod
    def do_mission(self):
        pass
    
class AerialVehicle(metaclass=ABCMeta):
    """ A vehicle made for ground fields."""
    def use_radar(self):
        print("I use my radar !")

class GroundVehicle(metaclass=ABCMeta):
    """ A vehicle made for ground fields."""
    def use_lidar(self):
        print("I use my lidar !")
    
class UnderseaVehicle(metaclass=ABCMeta):
    """ A vehicle made for ground fields."""
    def use_sonar(self):
        print("I use my sonar !")

    

class UAV(UnmannedVehicle, AerialVehicle):
    """Unmanned Aerial Vehicle"""
    def do_mission(self):
        print("I take off, I go to my mission, I land to base !")

class UGV(UnmannedVehicle, GroundVehicle):
    """Unmanned Ground Vehicle"""
    def do_mission(self):
        print("I move underwater, I go to my mission, I go back at the surface !")

class UUV(UnmannedVehicle, UnderseaVehicle):
    """Unmanned Undersea Vehicle"""
    def do_mission(self):
        print("I go underwater, I go to my mission, I land to base !")




if __name__ == '__main__':
    uav = UAV()
    uav.do_mission()
    uav.use_radar()

    ugv = UGV()
    ugv.do_mission()
    ugv.use_lidar()

    uuv = UUV()
    uuv.do_mission()
    uuv.use_sonar()

