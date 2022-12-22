import doctest


class Cookies:
    def __init__(self, quantity: int, taste: str):
        """
        Создание и подготовка к работе объекта "Печеньки"
        :param quantity: Количество печенек
        :param taste: Вкус/тип печенек
        Примеры:
        >>> cookies = Cookies(10, 'oatmeal')  # инициализация экземпляра класса
        """
        if not isinstance(quantity, int):
            raise TypeError("Количество должно быть типа int")
        if quantity <= 0:
            raise ValueError("Количество должно быть положительным числом")
        self.quantity = quantity

        if not isinstance(taste, str):
            raise TypeError("Содержимое должно быть str")
        self.taste = taste

    def eat_cookies(self, number) -> int:
        """
        Функция которая ест печеньки
        :param number: Сколько съесть
        :raise TypeError: Есть можно целое количество печенек
        :raise ValueError: Хотите съесть слишком много/мало печенек
        :return: Оставшиеся печеньки
        Примеры:
        >>> cookies = Cookies(10, 'oatmeal')
        >>> cookies.eat_cookies(5)
        """
        if not isinstance(number, int):
            raise TypeError("Число печенек должно быть типа int")
        if number < 0:
            raise ValueError("Число печенек должно быть > 0")
        if number > self.quantity:
            raise ValueError("Хотите съесть слишком много печенек")
        ...

    def add_cookies(self, number) -> int:
        """
        Функция которая добавляет печеньки
        :param number: Сколько добавить
        :raise TypeError: Есть можно целое количество печенек
        :raise ValueError: Число печенек должно быть > 0
        :return: Число печенек
        Примеры:
        >>> cookies = Cookies(10, 'oatmeal')
        >>> cookies.add_cookies(5)
        """
        if not isinstance(number, int):
            raise TypeError("Число печенек должно быть типа int")
        if number < 0:
            raise ValueError("Число печенек должно быть > 0")
        ...

    def change_taste(self, taste: str) -> None:
        """
        Изменение содержимиго бутылки
        :param taste: Вкус/тип печенек
        :raise TypeError: Вкус/тип печенек должен быть str
        Примеры:
        >>> cookies = Cookies(10, 'oatmeal')
        >>> cookies.change_taste('chocolate')
        """
        if not isinstance(taste, str):
            raise TypeError("Вкус/тип должен быть типа str")
        ...


class Lamp:
    def __init__(self, brightness: float, is_on: bool):
        """
        Создание и подготовка к работе объекта "Лампа"
        :param brightness: Яркость
        :param is_on: Включена ли лампа
        Примеры:
        >>> lamp = Lamp(500, False)  # инициализация экземпляра класса
        """
        if not isinstance(brightness, (int, float)):
            raise TypeError("Яркость должна быть типа int или float")
        if brightness <= 0:
            raise ValueError("Яркость должна быть положительным числом")
        self.brightness = brightness

        if not isinstance(is_on, bool):
            raise TypeError("Состояние должно быть bool")
        self.is_on = is_on

    def is_glowing(self) -> bool:
        """
        Функция, которая проверяет светит ли лампа (включена и яркость > 0)
        :return: Свеит ли лампа
        Примеры:
        >>> lamp = Lamp(500, False)
        >>> lamp.is_glowing()
        """
        ...

    def lamp_on(self) -> None:
        """
        Функция, которая включает лампу
        Примеры:
        >>> lamp = Lamp(500, False)
        >>> lamp.lamp_on()
        """
        ...

    def lamp_off(self) -> None:
        """
        Функция, которая выключает лампу
        Примеры:
        >>> lamp = Lamp(500, True)
        >>> lamp.lamp_off()
        """
        ...


class Bottle:
    def __init__(self, volume: float, content: str):
        """
        Создание и подготовка к работе объекта "Бутылка"
        :param volume: Объем бутылки
        :param content: Содержимое
        Примеры:
        >>> bottle = Bottle(500, 'vine')  # инициализация экземпляра класса
        """
        if not isinstance(volume, (int, float)):
            raise TypeError("Объем должен быть типа int или float")
        if volume <= 0:
            raise ValueError("Объем должен быть положительным числом")
        self.capacity_volume = volume

        if not isinstance(content, str):
            raise TypeError("Содержимое должно быть str")
        self.occupied_volume = content

    def is_alcohol(self) -> bool:
        """
        Функция которая проверяет является ли напиток алкогольным
        :return: Является ли напиток алкогольным
        Примеры:
        >>> bottle = Bottle(500, 'vine')
        >>> bottle.is_alcohol()
        """
        ...

    def is_zero_sugar(self) -> bool:
        """
        Функция которая проверяет является ли напиток диетическим
        :return: Является ли напиток алкогольным
        Примеры:
        >>> bottle = Bottle(500, 'coca-cola zero')
        >>> bottle.is_zero_sugar()
        """
        ...

    def change_content(self, content: str) -> None:
        """
        Изменение содержимиго бутылки
        :param content: Содержимое бутылки
        :raise ValueError: Если количество добавляемой жидкости превышает свободное место в стакане, то вызываем ошибку
        Примеры:
        >>> bottle = Bottle(500, 'vine')
        >>> bottle.change_content('juice')
        """
        if not isinstance(content, str):
            raise TypeError("Содержимое должно быть типа str")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации