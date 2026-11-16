class Car:
  def move(self):
    print("The car drives on the road")

class Boat:
  def move(self):
    print("The boat sails on water")

class Drone:
  def move(self):
    print("The drone flies in the sky")

def start_trip(vehicle):
  vehicle.move

my_car = Car()
my_boat = Boat()
my_drone = Drone()

start_trip(my_car)
start_trip(my_boat)
start_trip(my_drone)
