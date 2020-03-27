import numpy as np
import random as rd
import math
import heapq
import matplotlib.pyplot as plt


#### Leyenda:
#### sexo: M de masculino y F de femenino
#### estado: S de soltero, C de Casado y V de viudo

def Uniforme(inf,sup):
    return np.random.uniform(inf,sup)

def Exp(l):
    u = np.random.uniform(0,1)
    return -(1/l)*math.log(u)

#Probabilidad de fallecer dependiendo de la edad y el sexo-------Uniforme
def PF(edad,sexo):
    if sexo=="M":
        if edad < 12: return 0.02
        if edad < 45: return 0.1
        if edad < 76: return 0.3
        if edad <= 125: return 0.4
    else:
        if edad < 12: return 0.02
        if edad < 45: return 0.1
        if edad < 76: return 0.3
        if edad <= 125: return 0.4

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
    if valor <= 0.05: return rd.randrange(6,10)
    if valor <= 0.1: return 5
    if valor <= 0.2: return 4
    if valor <= 0.35: return 3
    if valor <= 0.6: return 1
    if valor <= 0.75: return 2
    else: return 0

#Probabilidad de desear pareja segun la edad-------------Uniforme
def DesearPareja(edad):
    if 12 <= edad <15: return 0.6
    if 15 <= edad <21: return 0.65
    if 21 <= edad <35: return 0.8
    if 35 <= edad <45: return 0.6
    if 45 <= edad <60: return 0.5
    if 60 <= edad <=125: return 0.2
    return 0

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
    else: return "F"

class Persona:
    def __init__(self,idc,sexo):
        self.id=idc
        self.edad=1
        self.sexo=sexo
        self.estado="S"
        self.CantHijos=0
        u=Uniforme(0,1)
        self.NMHijos=HijosDeseados(u)
        self.embarazada=False
        self.pornacer=0
        self.me=0    #esta variable es para cuando embarazada=true empezar a contar el numero de meses
        self.muerto=False
        self.dtp=False  ##deseo de tener pareja
        self.PeriodoSola=0
        self.idPareja=0
    
    ##Este metodo es para Actualizar las variables que necesitan cambios por la edad
    def Actualiza(self):
        u=Uniforme(0,1)
        f=PF(self.edad,self.sexo)
        if(u<=f):
            self.muerto=True
        y=Uniforme(0,1)
        if(y <= DesearPareja(self.edad)):
            self.dtp=True
        if self.PeriodoSola >0:
            self.PeriodoSola= self.PeriodoSola-1
        
        
        


#Ahora pasemos a definir las listas y las variables que necesitamos

class Simulacion():
    def __init__(self,m,h):
        self.personas={}
        self.fallecidos={}
        self.tiempo=0
        self.mesesActuales=0
        self.annostranscurridos=0
        self.CTEmbarazos=0
        self.CAEmbarazadas=0
        self.CRupturas=0
        self.CFallecidos=0
        self.CEmparejamientos=0
        self.CEMultiples=0
        self.CNacimientos=0
        self.PoblacionT=0
        self.TFinal=100
        self.bebes={}
        self.Inicialmente(m,h)


    def Inicialmente(self,m,h):
        self.PoblacionT=m+h
        for i in range(m):
            idp=rd.randint(0,2**31)
            P=Persona(idp,"M")
            self.personas[idp]=P
        for i in range(h):
            idp=rd.randint(0,2**31)
            P=Persona(idp,"F")
            self.personas[idp]=P
        self.mesesActuales=1
        self.tiempo=1



    def SimularPoblacion(self):
        for i in range(1,self.TFinal):
            for p in self.personas:
                self.personas[p].edad=self.personas[p].edad + 1
                self.personas[p].Actualiza()

            #Evento "Fallecer"
            for p in self.personas:
                if self.personas[p].muerto==True:            
                    self.fallecidos[p]=self.personas[p]
                    self.CFallecidos=self.CFallecidos+1
                    #Si era casado, poner a la pareja en viud@ y actualizar el time de Soledad(Luto)
                    if self.personas[p].estado=="C":
                        self.personas[p].estado="M"
                        print("Fallecio un casado")
                        self.personas[self.personas[p].idPareja].estado="V"
                        print(self.personas[self.personas[p].idPareja].estado)
                        self.personas[self.personas[p].idPareja].PeriodoSola=PeriodoSoledad(self.personas[self.personas[p].idPareja].edad)
                        self.personas[self.personas[p].idPareja].idPareja=0
                        self.personas[p].idPareja=0

                        print(self.personas[p].idPareja)
                    #P=self.personas.pop(self.personas[p].id)
            
            for p in self.fallecidos:
                if self.personas.__contains__(p)==True: 
                    self.personas.pop(p)
                    

            while self.mesesActuales <= 12 and self.personas.__len__()>0:
                #Aqui le daremos seguimieto a las embarazadas y Al evento "Nacer"
                for b in self.bebes:
                    self.personas[b]=self.bebes[b]
                self.bebes.clear()

                print(self.personas.__len__())
                for p in self.personas:
                    if(self.personas[p].embarazada==True):
                        #primero vamos a agregarle el contador a los meses de las embarazadas
                        if self.personas[p].me < 9:
                            self.personas[p].me = self.personas[p].me + 1
                        else:
                            #Ha nacido una persona
                            for j in range(self.personas[p].pornacer):
                                idp=rd.randint(0,2**31)
                                sexo=SeleccionSexo()
                                P=Persona(idp,sexo)           
                                self.bebes[idp]=P
                                self.CNacimientos=self.CNacimientos+1
                                self.CAEmbarazadas=self.CAEmbarazadas-1
                                print("Nacio ALguien por tu vida!!")
                            self.personas[p].embarazada=False
                            self.personas[p].me=0
                            self.personas[p].pornacer=0
                    
                    #Evento Embarazar:   
                    if self.personas[p].estado=="C":
                        print(self.personas[p].estado)
                        print(str(self.annostranscurridos)+" "+str(self.tiempo))
                        num=self.personas[p].idPareja
                        print(self.personas[num].id)
                        if (self.personas[p].NMHijos-self.personas[p].CantHijos>1) and (self.personas[self.personas[p].idPareja].NMHijos-self.personas[self.personas[p].idPareja].CantHijos>1):
                            u=Uniforme(0,1)
                            if(u <= PE(self.personas[p].edad)):
                                self.personas[p].embarazada=True
                                self.personas[p].me=1
                                y=Uniforme(0,1)
                                self.personas[p].pornacer=EmbarazoMultiple(y)
                                self.CTEmbarazos=self.CTEmbarazos+1
                                self.CAEmbarazadas=self.CAEmbarazadas+1
                                if self.personas[p].pornacer>1: self.CEMultiples= self.CEMultiples+1
                                
                    #Evento Ruptura
                    if self.personas[p].estado=="C":
                        print(self.personas[p].estado)
                        u=Uniforme(0,1)
                        if(u<=ProbabilidadRuptura()):
                            print("Rompieron!!!!!")
                            self.personas[p].estado="S"
                            
                            self.personas[p].PeriodoSola=Exp(PeriodoSoledad(self.personas[p].edad))
                            self.personas[self.personas[p].idPareja].estado="S"
                            print(self.personas[p].estado)
                            print(self.personas[self.personas[p].idPareja].estado)
                            
                            self.personas[self.personas[p].idPareja].PeriodoSola=Exp(PeriodoSoledad(self.personas[self.personas[p].idPareja].edad))
                            self.personas[self.personas[p].idPareja].idPareja=0
                            self.personas[p].idPareja=0
                            self.CRupturas=self.CRupturas+1

                    #Evento Emparejar:
                    if self.personas[p].sexo=="F" and self.personas[p].estado=="S" and self.personas[p].PeriodoSola < 1:
                        for h in self.personas:
                            if self.personas[h].sexo=="M" and self.personas[h].estado=="S" and self.personas[h].PeriodoSola < 1:
                                u=Uniforme(0,1)
                                dif=abs(self.personas[p].edad-self.personas[h].edad)
                                if(self.personas[p].dtp==True and self.personas[h].dtp==True and u <= EstablecerPareja(dif)):
                                    self.personas[p].estado="C"
                                    self.personas[h].estado="C"
                                    self.personas[p].idPareja=self.personas[h].id
                                    self.personas[h].idPareja=self.personas[p].id
                                    self.CEmparejamientos=self.CEmparejamientos+1
                                    print("Empareje!!")
                
                    self.mesesActuales=self.mesesActuales+1
                    self.tiempo=self.tiempo+1
            
            self.mesesActuales=1
            self.annostranscurridos=self.annostranscurridos+1




def Main():
    
    Mujeres=50
    Hombres=50
   # Variables()
   # Inicialmente(Mujeres,Hombres)
   # SimularPoblacion()
    Poblacion=Simulacion(Mujeres,Hombres)
    Poblacion.SimularPoblacion()
    
    print(Poblacion.CNacimientos)
    print(Poblacion.CFallecidos)
    


Main()
                






    



















