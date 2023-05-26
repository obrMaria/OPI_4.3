#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Составить программу с использованием иерархии классов. Номер варианта необходимо
получить у преподавателя. В раздел программы, начинающийся после инструкции if __name__= '__main__':
добавить код, демонстрирующий возможности разработанных классов.
1. Создать базовый класс Car (машина), характеризуемый торговой маркой (строка), числом цилиндров, мощностью.
Определить методы переназначения и изменения мощности. Создать производный класс Lorry   (грузовик),
характеризуемый также грузоподъемностью кузова. Определить функции переназначения марки и изменения
грузоподъемности.

"""



class Car:
    def __init__(self, mark, cylinders, power):
        self.__mark = mark
        self.__cylinders = cylinders
        self.__power = power

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, inp):
        self.__mark = inp

    @property
    def cylinders(self):
        return self.__cylinders

    @cylinders.setter
    def cylinders(self, inp):
        self.__cylinders = inp

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, inp):
        self.__power = inp


class Lorry(Car):
    def __init__(self, mark, cylinders, power, capacity):
        super().__init__(mark, cylinders, power)
        self.__capacity = capacity

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, inp):
        self.__capacity = inp


if __name__ == "__main__":
    truck = Lorry("Газель", 4, 119, 2500)
    passenger = Car("Лада", 8, 105)
    print(f"Марка {truck.mark}, количество цилиндров: {truck.cylinders}, "
          f"мощность: {truck.power} л.с, грузоподъемность: {truck.capacity} т")
    print(f"Марка {passenger.mark}, количество цилиндров: {passenger.cylinders}")


