class Barrio:

    def __init__(self, pos_1, pos_2, pos_3, pos_4, nombre):
        self.__pos_1 = pos_1
        self.__pos_2 = pos_2
        self.__pos_3 = pos_3
        self.__pos_4 = pos_4
        self.__nombre = nombre

    def getPos_1(self):
        return self.__pos_1

    def setPos_1(self, pos_1):
        self.__pos_1 = pos_1

    def getPos_2(self):
        return self.__pos_2

    def setPos_2(self, pos_2):
        self.__pos_2 = pos_2

    def getPos_3(self):
        return self.__pos_3

    def setPos_3(self, pos_3):
        self.__pos_3 = pos_3

     def getPos_4(self):
        return self.__pos_4

    def setPos_4(self, pos_4):
        self.__pos_4 = pos_4

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre
