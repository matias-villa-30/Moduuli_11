class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = tämänhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka

    def drive(self, time):
        self.kuljettu_matka += self.tämänhetkinen_nopeus * time


class ElectricCar(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, battery_capacity):
        super().__init__(rekisteritunnus, huippunopeus)
        self.battery_capacity = battery_capacity

    def print_info(self):
        return "{} {} km/h {} kWh".format(self.rekisteritunnus, self.huippunopeus, self.battery_capacity)


class GasolineCar(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, fuel_tank_capacity):
        super().__init__(rekisteritunnus, huippunopeus)
        self.fuel_tank_capacity = fuel_tank_capacity

    def print_info(self):
        return "{} {} km/h {} liters".format(self.rekisteritunnus, self.huippunopeus, self.fuel_tank_capacity)


def main():
    auto_electrico = ElectricCar("ABC-15", 180, 52.5)
    auto_gasolina = GasolineCar("ACD-123", 165, 32.3)

    auto_electrico.tämänhetkinen_nopeus = 120  # Electric car speed (in km/h)
    auto_gasolina.tämänhetkinen_nopeus = 100  # Gasoline car speed (in km/h)


    auto_electrico.drive(3)
    auto_gasolina.drive(3)


    print("Electric car ({}): {} km".format(auto_electrico.rekisteritunnus, auto_electrico.kuljettu_matka))
    print("Gasoline car ({}): {} km".format(auto_gasolina.rekisteritunnus, auto_gasolina.kuljettu_matka))



main()
