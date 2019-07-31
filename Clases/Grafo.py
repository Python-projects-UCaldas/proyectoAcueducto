import pygame,sys
from pygame.locals import *

class Grafo:
    def __init__(self):
        self.__vertices = []
        self.__aristas=[]

    def setVertices(self,listaVertice):
        self.__vertices = listaVertice

    def setAristas(self,listaArista):
        self.__aristas = listaArista
 
    def agregarVertice(self, vertice):
        self.__vertices.append(vertice)

    def agregarArista(self, arista):
        self.__aristas.append(arista)
 
    def getVertice(self, vertice):
        for vert in self.__vertices:
            if(vert == vertice):
                return vert

    def getArista(self, origen, destino):
        for arist in self.__aristas:
            if(arist.getOrigen() == origen and arist.getDestino() == destino):
                return arist

    def getVertice(self, key):
        for vert in self.__vertices:
            if(key == vert.getID()):
                return vert

    def invertirArist(self, origen, destino):
        for i in self.__aristas:
            if (i.getOrigen() == origen and i.getDestino() == destino):
                i.invertirArista(origen, destino)

    def getAristaOrigen(self, origen):
        lista = []
        for i in self.__aristas:
            if(origen == i.getOrigen()):
                lista.append(i.getDestino())
        return(lista)

    def getDestinoArista(self, origen):
        lista = []
        destino = self.getAristaOrigen(origen)
        destino2 = ''
        for j in destino:
            destino2 = j
            for i in self.__aristas:
                if(origen == destino2):
                    lista.append(i.getDestino()) 
        return lista

    def busquedaAnchura(self, origen):
        anchuraLista = []
        visitados = {}
        cola = []
        for i in self.__vertices:
            visitados.update({i.getID():False})
        cola.append(origen)
        visitados[origen]= True
        
        while cola:
            origen = cola.pop(0)
            # if (self.__aristas.getArista(origen, cola)):
            anchuraLista.append(origen)

            for i in self.getVertice(origen).getAdyacencias():
                for j in i.keys():
                    if visitados[j] == False:
                        cola.append(j)
                        visitados[j] = True
        return anchuraLista

    def camino(self, origen, destino):
        lista = self.busquedaAnchura(origen)
        if (origen in lista and destino in lista):
            return True
        else:
            return False

    def flujoMaximo(self, origen, destino, pesos):
        try:
            for i in self.__vertices:
                if(i.getID() == origen):
                    a = i.getMayorPesoArista()
                    pesos.append(a)
                    self.flujoMaximo(i.getMayorPesoAristaV(), destino, pesos)
                    b = min(pesos)
                    for j in range(0, (len(pesos))):
                        pesos[j] = pesos[j] - b
                    print(pesos)

            while self.camino(origen, destino):
                pass

        except:
            print('error')
            #pesos[len(pesos)] = pesos[len[pesos]] - min(pesos)

    def floydWarshall(self, origen, destino):
        Madyacencias = []
        Madyacencias1 = []
        Mpesos = []
        Mpesos1 = []
        aux=[]

        for i in range(0,len(self.__aristas)):
            for j in range(0, len(self.__aristas)):
                if i != j and self.__aristas[i].getPeso()< self.__aristas[j].getPeso():
                    aux = self.__aristas[i]
                    self.__aristas[i] = self.__aristas[j]
                    self.__aristas[j] = aux

        auxCambioPesos = {}
        for m in range(0,len(self.__aristas)):
                auxCambioPesos[self.__aristas[m].getPeso()] = self.__aristas[len(self.__aristas)-1-m].getPeso()
        

        # for i in range (0,len(self.__aristas)):
        #     for j in auxCambioPesos:
        #         if(self.__aristas[i].getPeso()==j):
        #             self.__aristas[i].setPeso(auxCambioPesos[j])
       
        for j in range(0, len(self.__vertices)):
            Madyacencias1.append(self.__vertices[j].getID())
        for i in range(0, len(self.__vertices)):
            Madyacencias.append(Madyacencias1.copy())
        print(Madyacencias)
        listas = []

        for i in range(0, len(self.__vertices)):
            Mpesos = []
            for j in range(0, len(self.__vertices)):
                if(self.existeArista(self.__vertices[i].getID(),self.__vertices[j].getID())):
                    Mpesos.append(auxCambioPesos[self.pesoArista(self.__vertices[i].getID(),self.__vertices[j].getID())])
                elif(i==j):
                    Mpesos.append(0)
                else:
                    Mpesos.append(float("inf"))
            Mpesos1.append(Mpesos.copy()) 
        #print(Mpesos1)    
       #listas=self.crearMatriz(Mpesos)
        

        for i in range (0, len(self.__vertices)):
            for j in range (0, len(self.__vertices)):
                for k in range (0, len(self.__vertices)):
                    if j != i and k != i:
                        if Mpesos1[j][k] > (Mpesos1[j][i]+Mpesos1[i][k]):
                            Mpesos1[j][k] = Mpesos1[j][i] + Mpesos1[i][k]
                            Madyacencias[j][k] = self.__vertices[i].getID()
        #print(listas)
        
        print(Madyacencias)
        print("---------")
        print(self.getRutas(Madyacencias, destino))

    def crearMatriz(self, matriz):
        matriz1=[]
        while(matriz):
            matriz1.append(matriz[:8])
            matriz=matriz[8:]
        return matriz1

    def existeArista(self, origen, destino):
        boolean = False
        for i in self.__aristas:
            if(i.getOrigen() == origen and i.getDestino() == destino and i.getActiva()):
                boolean = True
        return boolean

    def pesoArista(self, origen, destino):
        peso = "infi"
        for i in range(0, len(self.__aristas)):
            if (self.__aristas[i].getOrigen()==origen and self.__aristas[i].getDestino()== destino and self.__aristas[i].getActiva()):
                peso = self.__aristas[i].getPeso()
        return peso

    def getIndice(self, destino):
        for i in range (0,len(self.__vertices)):
            if (destino == self.__vertices[i].getID()):
                return i

    def getRutas(self,adyacencias, destino):
        indice = self.getIndice(destino)
        salida = []
        for n in self.__vertices:
            aux = []
            origen = n.getID()
            aux.append(origen)
            #tubo = self.__aristas.get((origen, adyacencias[self.getIndice(origen)][indice]))
            print(adyacencias[self.getIndice(origen)][indice])
            while self.existeArista(origen, adyacencias[self.getIndice(origen)][indice]):
                #print(n.getID())                
                origen = adyacencias[self.getIndice(origen)][indice]
                aux.append(origen)
                if origen == destino:
                   salida.append(aux)
                   #break
        return salida
