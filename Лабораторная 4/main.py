class Car:
    """Базовый класс, описывающий машины"""
    def __init__(self, color: str, build_year: int):
        self.color = color
        self.build_year = build_year

    def __repr__(self) -> str:
        """Печатаемое формальное представление объекта"""
        return f'{self.__class__.__name__}(color={self.color})'

    def __str__(self) -> str:
        """Преобразование объекта к строковому типу"""
        return f'{self.color} {self.__class__.__name__}'

    def years_old(self) -> int:
        """Вычисление возраста машины, используя год выпуска и текущее время системы"""
        pass

    def is_too_old(self) -> bool:
        """Определение, является ли машина старой"""
        if self.years_old() > 10:
            return True
        else:
            return False


class Truck(Car):
    """Дочерний класс, описывающий грузовые машины"""
    def __init__(self, load_capacity: float, color: str, build_year: int):
        super().__init__(color, build_year)
        self.load_capacity = load_capacity

    def __repr__(self):
        """Печатаемое формальное представление объекта"""
        return f'{self.__class__.__name__}(color={self.color}, build_year={self.build_year}, load_capacity={self.load_capacity})'

    def is_too_old(self) -> bool:
        """Определение, является ли машина старой"""
        if self.years_old() > 20:
            return True
        else:
            return False


class Crossover(Car):
    """Дочерний класс, описывающий кроссоверы"""
    def __init__(self, color: str, build_year: int):
        super().__init__(color, build_year)
