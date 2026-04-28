from main import TV, Fridge, Laptop, Apartment
import pytest


# створення даних
def setup_apartment():
    apartment = Apartment()
    apartment.add_appliance(TV("TV", 150, 0.8))
    apartment.add_appliance(Fridge("Fridge", 300, 0.3))
    apartment.add_appliance(Laptop("Laptop", 100, 0.5))
    return apartment


# тест додавання
def test_add_appliance():
    apartment = setup_apartment()
    assert len(apartment.appliances) == 3


# тест потужності
def test_total_power():
    apartment = setup_apartment()
    assert apartment.total_power() == 550


# тест сортування
def test_sort_by_power():
    apartment = setup_apartment()
    apartment.sort_by_power()
    powers = [a.power for a in apartment.appliances]
    assert powers == [100, 150, 300]


# тест пошуку
def test_find_by_radiation():
    apartment = setup_apartment()
    result = apartment.find_by_radiation(0.4, 1.0)
    names = [a.name for a in result]

    assert "TV" in names
    assert "Laptop" in names
    assert "Fridge" not in names


# тест помилки
def test_wrong_type():
    apartment = Apartment()
    with pytest.raises(TypeError):
        apartment.add_appliance("not appliance")
