class Transport:
    pass


class WaterTransport(Transport):  # Водный транспорт
    pass


class Boats(WaterTransport):  # Катера
    pass


class Steamboats(WaterTransport):  # Пароходы
    pass


class Sailboats(WaterTransport):  # Парусники
    pass


class AirTransport(Transport):  # Воздушный транспорт
    pass


class Aviation(AirTransport):  # Авиация
    pass


class Airplane(Aviation):  # Самолёт
    pass


class ToniStarksCostumes(Aviation):  # Костюмы Тони Старка
    pass


class Aeronautics(AirTransport):  # Воздухоплавание
    pass


class Airships(Aeronautics):  # Дирижабли
    pass


class Balloon(Aeronautics):  # Воздушные шары
    pass


class GroundTransport(Transport):  # Наземный транспорт
    pass


class Railway(GroundTransport):  # Железнодорожный
    pass


class Trains(Railway):  # Поезда
    pass


class Trams(Railway):  # Трамваи
    pass


class Automobile(GroundTransport):  # Автомобильный
    pass


class Tesla(Automobile):  # Тесла
    pass


class Ferrari(Automobile):  # Феррари
    pass


class Lamborgini(Automobile):  # Ламборгини
    pass


class BMW(Automobile):  # БМВ
    pass


class Cycling(GroundTransport):  # Велосипедный
    pass


class DrivenByAnimals(GroundTransport):  # Движимый животными
    pass


class Horse(DrivenByAnimals):  # Конный
    pass


class DogSled(DrivenByAnimals):  # Собачья упряжка
    pass


class SpaceTransport(Transport):  # Космический транспорт
    pass


class SpaceX(SpaceTransport):  # SpaceX
    pass


class RosKosmos(SpaceTransport):  # РосКосмос
    pass
