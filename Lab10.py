'''Створити клас “Сенсор” котрий містить поля:
- тип сенсора
- опис принципу роботи
- ціна
'''

class Sensor:

    colour = "black"

    def __init__(self, sensor_type = "", principle_of_work = "", price = 0, weight = 0, length = 0, width = 0):
        self.sensor_type = sensor_type
        self.principle_of_work = principle_of_work
        self.price = price
        self.weight = weight
        self.length = length
        self.width = width

    def __del__(self):
        print("Delete")

    def __str__(self):
        return str(self.__dict__)

    @staticmethod
    def get_static_field():
        return Sensor.colour

def main():
    sensor_1 = Sensor("motion sensor", "this sensor is triggered when it detects movement", 100, 50, 5, 3)
    sensor_2 = Sensor("light sensor", "this sensor is triggered when it detects light", 100, 30)
    sensor_3 = Sensor("sound sensor", "this sensor is triggered when it detects the sound", 100)
    print(sensor_1)
    print(sensor_2)
    print(sensor_3)
    print(Sensor.get_static_field())

if __name__ == '__main__':
    main()


