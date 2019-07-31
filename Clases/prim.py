#Creador: Eduardo Javier Maldonado Acevedo
#Carrera: Ingenieria en informatica
import os

class Prim:
    def __init__(self):
        self.grafo = {
"a":{"b":8,"c":10},
"b":{"f":1},
"c":{"b":20, "d":6,"f":5},
"d":{"e":7},
"e":{"c":1, "g":2},
"f":{"g":9},
"g":{"c":3, "h":15},
"h":{}
}

    def Menu(self):
        print (""">============= Algoritmo Prim ==============<
[1] Mostrar Grafo Completo
[2] Algoritmo Prim
[0] Salir
>===========================================<""")

    def seleccion(self):
        while True:
                #os.system("cls")
                g.Menu()
                opcion = input(">=> Ingresa tu opcion: ")
                if opcion=="1":
                 g.GrafoCompleto()
                elif opcion=="2":
                 raiz = input(">=> Ingresa el origen: ")
                 llave = self.grafo.keys()
                 if raiz not in llave:
                    print ("El origen no existe")
                    #os.system("pause")
                 else:
                    g.MetodoPrim(self.grafo,raiz)
                elif opcion=="0":
                    break
                else:
                 print ("No has ingresado una opcion correcta")
                 #os.system("pause")

    def MetodoPrim(self,grafo,raiz):
        cont = 0
        Ordenada = []
        Llave = list(grafo.keys())
        Llave.remove(raiz)
        visitados = [raiz]
        #print("==============================")
        #print ("Paso:",cont)
        #print ("==============================")
        #print ("Visitados:",visitados)
        #print ("Llaves:",Llave)
        #cont+=1
        resultante = {}
        destino = None

        while Llave:
            peso = float('inf')
            for s in visitados:
                for d in grafo[s]:
                        if d in visitados or s == d:
                            continue
                        if grafo[s][d] < peso:
                            peso = grafo[s][d]
                            origen = s
                            destino = d
            adyacentes = [(v, k) for k, v in grafo[s].items()]
            adyacentes.sort()
            adyacentes = [(v, k) for k, v in adyacentes]
            for i,k in adyacentes:
                Ordenada.append((visitados[-1],i,k))
            for a,b,c in Ordenada:
                if b in visitados:
                    Ordenada.remove((a,b,c))
            Ordenada = [(c,a,b) for a,b,c in Ordenada]
            Ordenada.sort()
            Ordenada = [(a,b,c) for c,a,b in Ordenada]
            #print ("Lista ordenada:",Ordenada)
            #print ("Adyacentes de",visitados[-1],":",adyacentes)
            if origen in resultante:
                if destino in resultante:
                    lista = resultante[origen]
                    resultante[origen] = lista+[(destino,peso)]
                    lista = resultante[destino]
                    lista.append((origen,peso))
                    resultante[destino] = lista
                else:
                    resultante[destino] = [(origen,peso)]
                    lista = resultante[origen]
                    lista.append((destino,peso))
                    resultante[origen] = lista
            elif destino in resultante:
                resultante[origen] = [(destino,peso)]
                lista = resultante[destino]
                lista.append((origen,peso))
                resultante[destino] = lista
            else:
                resultante[destino] = [(origen,peso)]
                resultante[origen] = [(destino,peso)]
            #print("==============================")
            #print ("Paso:",cont)
            #print ("==============================")
            visitados.append(destino)
            #print ("Visitados:",visitados)
            Llave.remove(destino)
            #print ("Llaves:",Llave)
            cont+=1
        print ("\n=========Resultados=========")
        print ("Visitados:",visitados)
        print ("Llaves:",Llave)
        while Ordenada:
            for a,b,c in Ordenada:
                if b in visitados:
                    Ordenada.remove((a,b,c))
        print ("Lista Ordenada:",Ordenada)
        print ("Arbol de expansion minima:")
        for key, lista in resultante.items():
            print (key)
            print (lista)
        print ("==============================")
        #os.system("pause")

    def GrafoCompleto(self):
        for key, lista in self.grafo.items():
            print (key)
            print (lista)
        #os.system("pause")

g = Prim()
g.seleccion()