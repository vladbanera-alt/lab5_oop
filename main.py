from abc import ABC, abstractmethod



class ElectricalAppliance(ABC):
    def __init__(self, name, power, radiation):
        self.name = name          # назва
        self.power = power        # потужність
        self.radiation = radiation  # радіація

    @abstractmethod
    def turn_on(self):
        pass


# тв
class TV(ElectricalAppliance):
    def turn_on(self):
        print(self.name + " увімкнений (ТВ)")


# холодильк
class Fridge(ElectricalAppliance):
    def turn_on(self):
        print(self.name + " увімкнений (Холодильник)")


# ноут
class Laptop(ElectricalAppliance):
    def turn_on(self):
        print(self.name + " увімкнений (Ноутбук)")


#квартира
class Apartment:
    def __init__(self):
        self.appliances = []  # список приладів

    # добавляємо прилад
    def add_appliance(self, appliance):
        if not isinstance(appliance, ElectricalAppliance):
            raise TypeError("неправильний тип")
        self.appliances.append(appliance)

    # увімкнення всіх
    def turn_on_all(self):
        for a in self.appliances:
            a.turn_on()

    # знаходження загальної потужність
    def total_power(self):
        total = 0
        for a in self.appliances:
            total += a.power
        return total

    #сортування
    def sort_by_power(self):
        self.appliances.sort(key=lambda x: x.power)

    #пошук по випромінюванню
    def find_by_radiation(self, min_val, max_val):
        result = []
        for a in self.appliances:
            if min_val <= a.radiation <= max_val:
                result.append(a)
        return result

    #вивід всіх приладів
    def print_all(self):
        for a in self.appliances:
            print(a.name, "потужність:", a.power)



def main():
    try:
        #створення квартири
        apartment = Apartment()

        # добавлення приладів
        apartment.add_appliance(TV("Samsung TV", 150, 0.8))
        apartment.add_appliance(Fridge("LG Fridge", 300, 0.3))
        apartment.add_appliance(Laptop("Dell Laptop", 65, 0.5))

        #увімкнення
        apartment.turn_on_all()

        #потужність
        print("загальна потужність:", apartment.total_power())

        #сортування
        apartment.sort_by_power()
        print("\nпісля сортування:")
        apartment.print_all()

        #пошук
        print("\nпошук (0.4 - 1.0):")
        result = apartment.find_by_radiation(0.4, 1.0)
        for a in result:
            print(a.name)

    except Exception as e:
        print("помилка:", e)


if __name__ == "__main__":
    main()
