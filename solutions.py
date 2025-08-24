class Car:
    def __init__(self, make, model, year, color, mpg):
        self.make = make
        self.model = model
        self.year = year
        self.mpg = mpg
        self.color = color
        self.fuel_level = 0.0  # in gallons

    def __str__(self):
        return f"{self.year} {self.make} {self.model}. Fuel level: {self.fuel_level} gallons. Gets {self.mpg} miles per gallon."
    def add_fuel(self, gallons):
        self.fuel_level += gallons
    def check_tank():
        return gallons
    def drive(self, miles) -> float:
        possible_miles = self.fuel_level * self.mpg
        if miles > possible_miles:
            miles = possible_miles
        self.fuel_level -= miles / self.mpg
        return miles
    def repaint(self, color):
        self.color = color


ol_reliable = Car("Toyota", "Sienna", 2017, "Silver", 30.3)
ol_reliable.add_fuel(12.3)
print(f"There are {ol_reliable.check_tank()} gallons left in the {ol_reliable}")
print(f"Let's try to drive 100 miles! We drove {drive(1000)} miles, and now there is {ol_reliable.check_tank()} gallons left in the tank.")
ol_reliable.repaint("Lime Green")
print(f"We've repainted our car! {ol_reliable}")