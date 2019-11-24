from easygui import *


class Set(EgStore):
    def __init__(self, value1, value2, filename):
        super().__init__(filename)
        self.value1 = value1
        self.value2 = value2
