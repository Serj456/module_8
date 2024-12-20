class IncorrectVinNumber(Exception):
    def __init__(self, message, info):
        self.message = message
        self.info = info
class IncorrectCarNumbers(Exception):
    def __init__(self, message, info):
        self.message = message
        self.info = info

class Car:
    def __init__(self, model, __vin, __numbers):
        self.model = model
        self.__vin = __vin
        self.__numbers = __numbers
        self.__is_valid_vin(__vin)
        self.__is_valid_numbers(__numbers)
    def __is_valid_vin(self, vin_number):
        if isinstance(vin_number, int):
            if vin_number >= 1000000 and vin_number <= 9999999:
                return True
            else:
                raise IncorrectVinNumber("Неверный диапазон для vin номера", 'vin_number' == vin_number)
            return True
        else:
            raise IncorrectVinNumber("Некорректный тип vin номер", 'vin_number' == vin_number)



    def __is_valid_numbers(self,numbers):
        if isinstance(numbers, str):
            if len(numbers) == 6:
                return True
            else:
                raise IncorrectCarNumbers("Неверная длина номера", "car_number" == numbers)
            return True
        else:
            raise IncorrectCarNumbers('Некорректный тип данных для номеров', "car_number" == numbers)








try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')