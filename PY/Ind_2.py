#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
В следующих заданиях требуется реализовать абстрактный базовый класс, определив в нем
абстрактные методы и свойства. Эти методы определяются в производных классах. В базовых
классах должны быть объявлены абстрактные методы ввода/вывода, которые реализуются в
производных классах.
Вызывающая программа должна продемонстрировать все варианты вызова переопределенных
абстрактных методов. Написать функцию вывода, получающую параметры базового класса по
ссылке и демонстрирующую виртуальный вызов.
    Создать абстрактный класс Currency (валюта) для работы с денежными суммами. Определить виртуальные функции
перевода в рубли и вывода на экран. Реализовать производные классы Dollar (доллар) и Euro (евро) со своими
функциями перевода и вывода на экран.
"""

from abc import ABC, abstractmethod

# Определение абстрактного класса Currency
class Currency(ABC):
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def to_rubles(self):
        pass

    @abstractmethod
    def display(self):
        pass


# Определение класса Dollar (доллар)
class Dollar(Currency):
    def __init__(self, amount):
        super().__init__(amount)

    def to_rubles(self):
        return self.amount * 75.0  # Пример конвертации: 1 доллар = 75 рублей

    def display(self):
        print(f"${self.amount}")


# Определение класса Euro (евро)
class Euro(Currency):
    def __init__(self, amount):
        super().__init__(amount)

    def to_rubles(self):
        return self.amount * 90.0  # Пример конвертации: 1 евро = 90 рублей

    def display(self):
        print(f"€{self.amount}")


if __name__ == "__main__":
    dollar = Dollar(10)
    euro = Euro(5)

    # Вызов методов класса Dollar
    dollar.display()
    rubles = dollar.to_rubles()
    print(f"In rubles: {rubles}")

    # Вызов методов класса Euro
    euro.display()
    rubles = euro.to_rubles()
    print(f"In rubles: {rubles}")
