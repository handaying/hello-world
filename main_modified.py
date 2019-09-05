from enum import Enum, unique
import math


@unique
class internal_types(Enum):
    tray = 0
    packing = 1


class section(object):
    def __init__(self):
        self.__internal_type = internal_types.tray
        self.__tray = tray()
        self.__packing = packing()

    @property
    def internal_type(self):
        return self.__internal_type

    @internal_type.setter
    def internal_type(self, value):
        if type(value) is internal_types:
            self.__internal_type = value
        else:
            raise TypeError("invalid value")

    @property
    def start_stage(self):
        return self.__start_stage

    @start_stage.setter
    def start_stage(self, value):
        self.__start_stage = value

    @property
    def end_stage(self):
        return self.__end_stage

    @end_stage.setter
    def end_stage(self, value):
        self.__end_stage = value

    @property
    def diameter(self):
        return self.__diameter

    @diameter.setter
    def diameter(self, value):
        self.__diameter = value
        self.__tray.diameter = self.__packing.diameter = value

    @property
    def cross_sectional_area(self):
        return math.pi/4 * self.__diameter * self.__diameter

    @property
    def internal(self):
        if self.internal_type == internal_types.tray:
            return self.__tray
        elif self.internal_type == internal_types.packing:
            return self.__packing


class tray(object):
    @property
    def number_of_passes(self):
        return self.__number_of_passes

    @number_of_passes.setter
    def number_of_passes(self, value):
        self.__number_of_passes = value

    @property
    def diameter(self):
        return self.__diameter

    @diameter.setter
    def diameter(self, value):
        self.__diameter = value


class packing(object):
    @property
    def diameter(self):
        return self.__diameter

    @diameter.setter
    def diameter(self, value):
        self.__diameter = value


if __name__ == "__main__":
    s = section()
    s.diameter = 10
    # s.internal_type = internal_types.tray
    # s.internal.number_of_passes = 1
    print(s.cross_sectional_area)
    print(s.internal.diameter)
