import pygame,sys 
import math
from pygame.locals import *

class  Arista(object):
	def __init__(self, origen, destino, peso, posOri, posDest, activa):
		self.__origen = origen
		self.__destino = destino
		self.__peso = peso
		self.__posOri = posOri
		self.__posDest = posDest
		self.__activa = activa

	def mostrarArista(self):
		print(self.__origen,self.__destino, self.__peso, self.__posOri, self.__posDest, self.__activa)

	def pintarArista(self, Surface):
		if(self.__activa):
			pygame.draw.line(Surface, (0,0,0), tuple(self.__posOri), tuple(self.__posDest), 5)
		else:
			pygame.draw.line(Surface, (250,0,0), tuple(self.__posOri), tuple(self.__posDest), 5)
		if(self.__posOri[0] == self.__posDest[0] and self.__posOri[1] > self.__posDest[1]):
			arriba = pygame.image.load("Recursos/flechas/arriba.png")
			arriba = pygame.transform.scale(arriba,(20,40))
			Surface.blit(arriba,(self.__posDest[0],(self.__posOri[1] - ((self.__posOri[1]-self.__posDest[1])/2))))
		elif(self.__posOri[0] == self.__posDest[0] and self.__posOri[1] < self.__posDest[1]):
			abajo = pygame.image.load("Recursos/flechas/abajo.png")
			abajo = pygame.transform.scale(abajo,(20,45))
			Surface.blit(abajo,(self.__posDest[0],(self.__posOri[1] - ((self.__posOri[1]-self.__posDest[1])/2))))
		elif(self.__posOri[0] < self.__posDest[0] and self.__posOri[1] == self.__posDest[1]):
			derecha = pygame.image.load("Recursos/flechas/derecha.png")
			derecha = pygame.transform.scale(derecha,(40,20))
			Surface.blit(derecha,((self.__posOri[0] - ((self.__posOri[0]-self.__posDest[0])/2)),self.__posDest[1]))
		elif(self.__posOri[0] > self.__posDest[0] and self.__posOri[1] == self.__posDest[1]):
			izquierda = pygame.image.load("Recursos/flechas/izquierda.png")
			izquierda = pygame.transform.scale(izquierda,(40,20))
			Surface.blit(izquierda,((self.__posOri[0] - ((self.__posOri[0]-self.__posDest[0])/2)),self.__posDest[1]))
		elif(self.__posOri[0] < self.__posDest[0] and self.__posOri[1] > self.__posDest[1]):
			arribaDerecha = pygame.image.load("Recursos/flechas/arribaDerecha.png")
			arribaDerecha = pygame.transform.scale(arribaDerecha,(36,36))
			Surface.blit(arribaDerecha,((self.__posOri[0] - ((self.__posOri[0]-self.__posDest[0])/2)),(self.__posOri[1] - ((self.__posOri[1]-self.__posDest[1])/2))))
		elif(self.__posOri[0] > self.__posDest[0] and self.__posOri[1] < self.__posDest[1]):
			abajoIzquierda = pygame.image.load("Recursos/flechas/abajoIzquierda.png")
			abajoIzquierda = pygame.transform.scale(abajoIzquierda,(36,36))
			Surface.blit(abajoIzquierda,((self.__posOri[0] - ((self.__posOri[0]-self.__posDest[0])/2)),(self.__posOri[1] - ((self.__posOri[1]-self.__posDest[1])/2))))
		elif(self.__posOri[0] > self.__posDest[0] and self.__posOri[1] > self.__posDest[1]):
			arribaIzquierda = pygame.image.load("Recursos/flechas/arribaIzquierda.png")
			arribaIzquierda = pygame.transform.scale(arribaIzquierda,(36,36))
			Surface.blit(arribaIzquierda,((self.__posOri[0] - ((self.__posOri[0]-self.__posDest[0])/2))-20,(self.__posOri[1] - ((self.__posOri[1]-self.__posDest[1])/2))))
		elif(self.__posOri[0] < self.__posDest[0] and self.__posOri[1] < self.__posDest[1]):
			abajoDerecha = pygame.image.load("Recursos/flechas/abajoDerecha.png")
			abajoDerecha = pygame.transform.scale(abajoDerecha,(36,36))
			Surface.blit(abajoDerecha,((self.__posOri[0] - ((self.__posOri[0]-self.__posDest[0])/2))-20,(self.__posOri[1] - ((self.__posOri[1]-self.__posDest[1])/2))))

		
	def getOrigen(self):
		return self.__origen

	def setOrigen(self, origen):
		self.__origen = origen

	def getDestino(self):
		return self.__destino

	def setDestino(self, destino):
		self.__destino = destino

	def getPosOrig(self):
		return self.__posOri
	
	def getPosDest(self):
		return self.__posDest

	def setPosOrig(self, posOri):
		self.__posOri = posOri

	def setPosDest(self, posDest):
		self.__posDest = posDest

	def getActiva(self):
		return self.__activa

	def setActiva(self, activa):
		self.__activa = activa

	def getPeso(self):
		return self.__peso

	def setPeso(self, peso):
		self.__peso = peso

	def modificarEstadoArist(self):
		if(self.getActiva()):
			self.__activa = False

		elif(not(self.getActiva())):
			self.__activa = True

	def invertirArista(self, origen, destino):
		temp = self.__posOri
		self.__posOri = self.__posDest
		self.__posDest = temp
		self.__origen = destino
		self.__destino = origen

	
