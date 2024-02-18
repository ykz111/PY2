class Computer_mouse:
    def __init__(self, mass: float, dpi: int, backlight_color: str):
        """
        Базовый класс. Описывает компьютерную мышь

        :param mass: Масса мыши в граммах
        :param dpi: dpi мыши
        :param backlight_color: Цвет подсветки мыши

        :raise TypeError: Если масса не является числом с плавающей точкой, dpi целым числом, а цвет подсветки строкой/
        вызовем ошибку
        :raise ValueError: Если масса или dpi меньше нуля вызовем ошибку

        Пример:
        >>> mouse_1 = Computer_mouse(100.9, 1600, "Red")
        """
        if not isinstance(mass, (int, float)):
            raise TypeError("Масса должна быть числом.")
        if mass <= 0:
            raise ValueError("Масса должна быть больше нуля.")
        self.mass = mass
        if not isinstance(dpi, int):
            raise TypeError("dpi должен быть целым числом.")
        if dpi <= 0:
            raise ValueError("dpi должен быть больше нуля.")
        self.dpi = dpi
        if not isinstance(backlight_color, str):
            raise TypeError("Цвет подсветки должен быть строчкой.")
        self.backlight_color = backlight_color

    def change_dpi(self, value: int, action: str) -> None:
        """
        Функция, позволяющая добавить или отнять dpi мыши

        :param value: На сколько dpi нужно изменить текущее значение
        :param action: Действие, которое необходимо совершить

        :raise TypeError: Если value не целое число вызовем ошибку
        :raise ValueError: Если value меньше нуля, value больше self.dpi, действие не add или subtract вызовем ошибку

        Пример:
        >>> mouse_1 = Computer_mouse(100.9, 1600, "Red")
        >>> mouse_1.change_dpi(100, "subtract")
        """
        if not isinstance(value, int):
            raise TypeError("Изменение dpi должно быть целым числом")
        if value <= 0:
            raise ValueError("Изменение dpi должно быть больше нуля")
        if self.dpi - value <= 0:
            raise ValueError("Окончательный dpi должен быть больше нуля")
        if action == "add":
            self.dpi += value
        if action == "subtract":
            self.dpi -= value
        else:
            raise ValueError("Действие должно быть add/subtract")
        return None

    def click(self) -> None:
        """
        Функция, позволяющая совершить клик мышкой

        Пример:
        >>> mouse_1 = Computer_mouse(100, 1600, "Red")
        >>> mouse_1.click()
        """
        ...

    def change_backlight_color(self, new_color: str) -> None:
        """
        Функция, позволяющая сменить цвет подсветки

        :param new_color: Цвет, на оторый меняется подсветка

        :raise TypeError: Если новый цвет не является строкой вызовем ошибку

        Пример:
        >>> mouse_1 = Computer_mouse(100.9, 1600, "Red")
        >>> mouse_1.change_backlight_color("Blue")
        """
        if not isinstance(new_color, str):
            raise TypeError("Новый цвет должен быть строкой")
        self.backlight_color = new_color
        return None

    def __str__(self) -> str:
        return f'Масса = {self.mass} г, dpi = {self.dpi}, цвет подсветки - {self.backlight_color}.'

    def __repr__(self):
        return f'{self.__class__.__name__}(mass={self.mass}, dpi={self.dpi}, bachlight_color={self.backlight_color})'


class Wireless_computer_mouse(Computer_mouse):
    def __init__(self, mass: float, dpi: int, backlight_color: str, connection_status: bool):
        """
        Производный класс. Описывает беспроводную компьютерную мышь

        :param connection_status: Статус подключения мыши

        :raise TypeError: Если статус подключение не типа bool вызовем ошибку

        Пример:
        >>> mouse_2 = Wireless_computer_mouse(100.9, 1600, "Red", True)
        """
        super().__init__(mass, dpi, backlight_color)
        if not isinstance(connection_status, bool):
            raise TypeError("Статус подключения должен быть типа bool")
        self.connection_status = connection_status

    def connect(self) -> None:
        """
        Функция, позволяющая подключить отключенную мышь

        :raise ValueError: Если мышь уже подключена вызовем ошибку

        Пример:
        >>> mouse_2 = Wireless_computer_mouse(100.9, 1600, "Red", False)
        >>> mouse_2.connect()
        """
        if not self.connection_status:
            self.connection_status = True
        else:
            raise ValueError("Мышь уже подключена")
        return None

    def unconnect(self) -> None:
        """
        Функция, позволяющая отключить подключенную мышь

        :raise ValueError: Если мышь уже отключена вызовем ошибку

        Пример:
        >>> mouse_2 = Wireless_computer_mouse(100.9, 1600, "Red", True)
        >>> mouse_2.unconnect()
        """
        if self.connection_status:
            self.connection_status = False
        else:
            raise ValueError("Мышь уже отключена")
        return None

    def click(self) -> None:
        """
        Перегружаем функцию, для клика нужно, чтобы мышь была подключена

        Пример:
        >>> mouse_2 = Wireless_computer_mouse(100, 1600, "Red", True)
        >>> mouse_2.click()
        """
        if not self.connection_status:
            raise ValueError("Мышь отключена")
        ...

    def __str__(self):
        return f'Масса = {self.mass} г, dpi = {self.dpi}, цвет подсветки - {self.backlight_color}, ' \
               f'статус подключения - {self.connection_status}.'

    def __repr__(self):
        return f'{self.__class__.__name__}(mass={self.mass}, dpi={self.dpi}, bachlight_color={self.backlight_color}, ' \
               f'connection_status={self.connection_status})'


if __name__ == "__main__":
    pass
