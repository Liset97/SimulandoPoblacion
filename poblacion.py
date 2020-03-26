import numpy as np
import random as rd
import math
import heapq
import matplotlib.pyplot as plt


#### Leyenda:
#### sexo: M de masculino y F de femenino

def Uniforme(inf,sup):
    return np.random.uniform(inf,sup)

def Exp(l):
    u = np.random.uniform(0,1)
    return -(1/l)*math.log(u)

#Probabilidad de fallecer dependiendo de la edad y el sexo-------Uniforme
def PF(edad,sexo):
    if sexo=="M":
        if edad < 12: return 0.25
        if edad < 45: return 0.1
        if edad < 76: return 0.3
        if edad <= 125: return 0.7
    else:
        if edad < 12: return 0.25
        if edad < 45: return 0.15
        if edad < 76: return 0.35
        if edad <= 125: return 0.65

#Probabilidad de que una mujer salga embaraza segun la edad----Uniforme
def PE(edad):
    if 12 <= edad <15: return 0.2
    if 15 <= edad <21: return 0.45
    if 21 <= edad <35: return 0.8
    if 35 <= edad <45: return 0.4
    if 45 <= edad <60: return 0.2
    if 60 <= edad <=125: return 0.05

#Dada una variable uniforme, determina el numero maximo de hijos
#que kiera tener una persona x
def HijosDeseados(valor):
    if valor <= 0.05: return random(6,10)
    if valor <= 0.1: return 5
    if valor <= 0.2: return 4
    if valor <= 0.35: return 3
    if valor <= 0.6: return 1
    if valor <= 0.75: return 2
    else return 0

#Probabilidad de desear pareja segun la edad-------------Uniforme
def DesearPareja(edad):
    if 12 <= edad <15: return 0.6
    if 15 <= edad <21: return 0.65
    if 21 <= edad <35: return 0.8
    if 35 <= edad <45: return 0.6
    if 45 <= edad <60: return 0.5
    if 60 <= edad <=125: return 0.2

def EstablecerPareja(diferencia):
    if diferencia < 5: return 0.45
    if diferencia < 10: return 0.4
    if diferencia < 15: return 0.35
    if diferencia < 20: return 0.25
    if diferencia >= 20: return 0.15

def ProbabilidadRuptura():
    #Si al tirar un random uniforme, este es menor que 0.2 entonces hay ruptura
    return 0.2

#Periodo de soledad en meses de una persona segun la edad dado que enviudo o se separo
#Sera una Exp de parametro lo que devuelva el metodo
def PeriodoSoledad(edad):
    if 12 <= edad < 15: return 3
    if 15 <= edad < 21: return 6
    if 21 <= edad < 35: return 6
    if 35 <= edad < 45: return 12
    if 45 <= edad < 60: return 24
    return 48

def EmbarazoMultiple(valor):
    if valor <= 0.02: return 5
    if valor <= 0.04: return 4
    if valor <= 0.08: return 3
    if valor <= 0.18: return 2
    if valor <= 0.7: return 1
    return 0

#Metodo que define el sexo de una persona mediante una variable uniforme
def SeleccionSexo():
    u = np.random.uniform(0,1)
    if u <= 0.5: return "M"
    else return "F"























