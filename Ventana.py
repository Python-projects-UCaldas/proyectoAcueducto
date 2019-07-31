import pygame,sys 
import os, json
from pygame.locals import*
from Clases import Arista
from Clases import Vertice
from Clases import Grafo
from VentanaAux import *
from PyQt5.QtWidgets import QApplication, QMainWindow


acueducto = Grafo()
listaVert=[]
listaArist=[]


def ventAux(grafo):
	class ventana(QMainWindow):

		def __init__(self):
			super(ventana, self).__init__()
			self.initUI()

		def initUI(self):
			self.ui = Ui_MainWindow()
			self.ui.setupUi(self)
			self.ui.floydWarshall.clicked.connect(lambda: grafo.floydWarshall())
			self.ui.InvertirArista.clicked.connect(lambda: grafo.invertirArist(self.ui.lineEditOrigenInvertir.text(), self.ui.lineEditDestinoInvertir.text()))
			self.ui.Actualizar.clicked.connect(lambda: pintar())
			self.show()	

	if __name__ == "__main__":
		aplicacion = QApplication(sys.argv)
		mi_app = ventana()
		sys.exit(aplicacion.exec_())

with open('Recursos/Acueducto.json', 'r', encoding="UTF-8") as contenido:
 	data = json.load(contenido)
 	for vertice in data["vertices"]:
 		ID = vertice["ID"]
 		capacidad=vertice["capacidad"]
 		posY=vertice["posY"]
 		posX = vertice["posX"]
 		barrio=vertice["barrio"]
 		adyacencias = vertice["adyacencia"]
 		vert = Vertice(ID, capacidad, adyacencias, posX, posY, barrio)
 		listaVert.append(vert)

 	for i in data["Aristas"]:
 		origen = i['origen']
 		destino = i['destino']
 		peso = i['peso']
 		posOri = i['posOri']
 		posDest = i['posDest']
 		activa = i['activa']
 		arist = Arista(origen, destino, peso, posOri, posDest, activa)
 		listaArist.append(arist)

acueducto.setVertices(listaVert)
acueducto.setAristas(listaArist)


acueducto.floydWarshall('a', 'c')
acueducto.invertirArist('a','c')
# acueducto.invertirArist('g', 'h')

# a=acueducto.getArista('a', 'c')
# a.modificarEstadoArist()
# pesos = []b
# acueducto.flujoMaximo('a', 'c', pesos)
#anchura = acueducto.busquedaAnchura('a')
#print(anchura)
# lista = acueducto.getDestinoArista('a')
# print(lista)


# b = acueducto.camino('e','c')
# print(b)

pygame.init()
ventana = pygame.display.set_mode((1280,800))
pygame.display.set_caption("RED DE ACUEDUCTO")
tanqueImagen = pygame.image.load("Recursos/tanque.png")
tanqueImagen = pygame.transform.scale(tanqueImagen,(72,72))
fondo = pygame.image.load("Recursos/mapa.png")
fondo = pygame.transform.scale(fondo,(1280,800))
	
ventana.blit(fondo, (0,0))
vertice = Vertice('z', 10, {"g":12}, 1153, 82, 'solferino')
vertice.pintarVertice(ventana, tanqueImagen)

def pintar():
	for i in listaArist:
		i.pintarArista(ventana)
		pygame.display.update()
		i.pintarArista(ventana)
		pygame.display.update()


	for i in listaVert:
		i.pintarVertice(ventana, tanqueImagen)	
		pygame.display.update()
		i.pintarVertice(ventana, tanqueImagen)

mifuente = pygame.font.Font(None, 30)

while True:
	posicion = pygame.mouse.get_pos()
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == K_a:
				ventAux(acueducto)
	contador = mifuente.render('Barrio solferino',0,(0,0,250))
	ventana.blit(contador,(100,100))
	pygame.display.update()