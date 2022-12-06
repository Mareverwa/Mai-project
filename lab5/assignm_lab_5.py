class Rocket:

    def __init__(self, weight, fuel):
        self.rocket_weight = weight
        self.fuel_weight = fuel
        self.engine_running = (fuel > 0)
    
    def spend_fuel(self, count):
        self.fuel_weight -= count
        
        if self.fuel_weight > 0:
            return True
        
        self.fuel_weight = 0
        self.engine_running = False
        return False
    
    def get_fuel_level(self):
        return self.fuel_weight
    
    def get_total_weight(self):
        return self.fuel_weight + self.rocket_weight

    def get_is_engine_running(self):
        return self.engine_running
    


sukhoi = Rocket(1000,500)
print("The total weight of the rocket is", sukhoi.get_total_weight())
sukhoi.spend_fuel(250)

print("The fuel level is ",sukhoi.get_fuel_level())
print("The engine is currently running ",sukhoi.get_is_engine_running())
print('The total weight is ',sukhoi.get_total_weight())

