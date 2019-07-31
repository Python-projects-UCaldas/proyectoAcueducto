import pygame,sys 
from pygame.locals import*

class Vertice(object):

    def __init__(self, ID, capacidad, adyacencias, posX, posY, barrio):
        self.__ID = ID
        self.__capacidad = capacidad
        self.__adyacencias = adyacencias
        self.__posX = posX
        self.__posY = posY
        self.__barrio = barrio

    def pintarVertice(self, Surface, tanqueImagen):
        Surface.blit(tanqueImagen,(self.__posX,self.__posY))
        mifuente = pygame.font.Font(None, 30)
        miTexto = mifuente.render(self.__ID,0,(200, 20 , 79))
        Surface.blit(miTexto,(self.__posX, self.__posY))
 
    def mostrarVertice(self):
        print(self.__ID, self.__capacidad, self.__adyacencias, self.__posX, self.__posY, self.__barrio)

    def getID(self):
        return self.__ID

    def setID(self, ID):
        self.__ID = ID

    def getCapacidad(self):
        return self.__capacidad

    def setCapacidad(self, capacidad):
        self.__capacidad = capacidad

    def getAdyacencias(self, ID):
        for adya in self.__adyacencias:
            if(adya.getID == ID):
                return adya

    def getMayorPesoArista(self):
        lista = []
        for i in self.__adyacencias:
            lista.append(list(i.values()))
        a = (max(lista))
        return a[0]

    def getMayorPesoAristaV(self):
        lista = []
        vertMayor = []
        for i in self.__adyacencias:
            lista.append(list(i.values()))
        for i in self.__adyacencias:
            if(max(lista) == (list(i.values()))):
                vertMayor.append(list(i.keys()))
        return(vertMayor[0][0])

    def getPosX(self):
        return self.__posX

    def setPosX(self, posX):
        self.__posX = posX

    def getPosY(self):
        return self.__posY

    def setPosY(self, posY):
        self.__posY = posY

    def getBarrios(self):
        return self.__barrio

    def setBarrios(self, barrio):
        self.__barrio.append(barrio)

    def getAdyacencias(self):
        return self.__adyacencias