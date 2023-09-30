from __future__ import annotations
from math import sqrt
# In Session 1, we talked about having classes as templates of objects.
# What if objects can EVOLVE and MORPH into other types?

# If I define a Truck. A race truck and a freight truck that both belong
# to a Truck parent class is not going to have the same usage. 
# This is why we use inheritance.
class Truck:
    def __init__(
            self, 
            weightKg: float, 
            manufacturer: str, 
            fuel_type: str,
            lifeKm: float = 0
            ) -> None:
        self.weightKg = weightKg
        self.manufacturer = manufacturer
        self.fuel_type = fuel_type
        self.lifeKm = lifeKm
        return
    def beep(self):
        print(f"Beep beep! I am a {self.manufacturer} truck that consumes {self.fuel_type}! I have done {self.lifeKm} Km!")

# RaceTruck inherits Truck, 
# and hence it contains all of Truck's methods and properties, 
# but also has its own unique method, race(), and property, accelerationMetersPerSec
class RaceTruck(Truck):
    def __init__(
            self, 
            weightKg: float, 
            manufacturer: str, 
            fuel_type: str,
            accelerationMetersPerSec: float,
            lifeKm: float = 0
            ) -> None:
        # Here below, the parent class is defined first
        super().__init__(weightKg, manufacturer, fuel_type, lifeKm)

        # Additional properties here
        self.accelerationMetersPerSec = accelerationMetersPerSec
        return
    # New method, unique to RaceTruck
    def race(self, otherRaceTruck: RaceTruck, distanceMeters: float):

        # Physics stuff... Don't worry about it too much
        selfTimeTakenSec = sqrt(2*distanceMeters/self.accelerationMetersPerSec)
        otherTimeTakenSec = sqrt(2*distanceMeters/otherRaceTruck.accelerationMetersPerSec)
        
        # Here, the property of the parent is modified 
        self.lifeKm += distanceMeters
        otherRaceTruck.lifeKm += distanceMeters
        
        # If the first truck uses less time to traverse the distance, it wins
        return selfTimeTakenSec < otherTimeTakenSec
    
# 2 different RaceTruck's that are based off the same class, but have different parameters
truck1 = RaceTruck(9000, "Mercedes-Benz", "Diesel", 0.8, 230)
truck2 = RaceTruck(9000, "Ford", "Petrol", 1.0, 67)

# Race time! Vroom vroom
truck1Wins = truck1.race(truck2, 1000)

if truck1Wins: 
    print("Truck 1 wins!")
    truck1.beep() # Methods from the parent class can still be referenced 
else: 
    print("Truck 2 wins!")
    truck2.beep() # Same here