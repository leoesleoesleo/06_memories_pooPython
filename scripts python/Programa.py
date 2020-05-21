# -*- coding: utf-8 -*-
"""
Created on Thu May  7 21:19:47 2020

@author: leonardo.patino
"""

from PacienteCovit import PacienteCovit
from PacienteGeneral import PacienteGeneral

while True:
    try:
        documento = input("Ingrese documento: ")
        if documento != "":
            break
        else:
            print("asegurese de colocar un documento válido") 
    except Exception as e:
            print("Error, asegurese de colocar un documento válido")   

while True:
    try:
        nombreCompleto = input("Ingrese nombre Completo: ")
        if nombreCompleto != "":
            break
        else:
            print("asegurese de colocar un nombreCompleto válido") 
    except Exception as e:
            print("Error, asegurese de colocar un nombreCompleto válido")   

while True:
    try:
        fechaNacimiento = input("Ingrese fechaNacimiento Completo: ")
        if fechaNacimiento != "":
            break
        else:
            print("asegurese de colocar un combreCompleto válido") 
    except Exception as e:
            print("Error, asegurese de colocar un combreCompleto válido")  

while True:
    try:
        temperatura = int(input("Ingrese temperatura: "))
        if temperatura >= 0:
            break
        else:
            print("asegurese de colocar un numero positivo")
    except Exception as e:
            print("No se permiten letras, asegurese de colocar un numero positivo")   

while True:
    try:
        enfermedadPresion = input("Ingrese enfermedadPresion (s:sí/n:no): ")
        if enfermedadPresion in ('s','n'):
            break
        else:
            print("asegurese de colocar un enfermedadPresion válido") 
    except Exception as e:
            print("Error, asegurese de colocar un enfermedadPresion válido")    

while True:
    try:
        enfermedadGlicemia = input("Ingrese enfermedadGlicemia (s:sí/n:no): ")
        if enfermedadGlicemia in ('s','n'):
            break
        else:
            print("asegurese de colocar un enfermedadPresion válido") 
    except Exception as e:
            print("Error, asegurese de colocar un enfermedadPresion válido")    
            
while True:
    try:
        tosSeca = input("Ingrese tosSeca (s:sí/n:no): ")
        if tosSeca in ('s','n'):
            break
        else:
            print("asegurese de colocar un tosSeca válido") 
    except Exception as e:
            print("Error, asegurese de colocar un tosSeca válido")   

while True:
    try:
        dificultadRespiratoria = input("Ingrese dificultadRespiratoria (s:sí/n:no): ")
        if dificultadRespiratoria in ('s','n'):
            break
        else:
            print("asegurese de colocar un dificultadRespiratoria válido") 
    except Exception as e:
            print("Error, asegurese de colocar un dificultadRespiratoria válido")   

while True:
    try:
        cansancioEscalofrio = input("Ingrese cansancioEscalofrio (s:sí/n:no): ")
        if cansancioEscalofrio in ('s','n'):
            break
        else:
            print("asegurese de colocar un dificultadRespiratoria válido") 
    except Exception as e:
            print("Error, asegurese de colocar un dificultadRespiratoria válido")   

while True:
    try:
        dolorCabezaGarganta = input("Ingrese dolorCabezaGarganta (s:sí/n:no): ")
        if dolorCabezaGarganta in ('s','n'):
            break
        else:
            print("asegurese de colocar un dificultadRespiratoria válido") 
    except Exception as e:
            print("Error, asegurese de colocar un dificultadRespiratoria válido")   
            
"""TEST
documento = '1017186651'
nombreCompleto = 'Leonardo Patiño'
fechaNacimiento = '11-11-1990'
enfermedadPresion = 'n'
enfermedadGlicemia = 'n'
tosSeca = 'n'
dificultadRespiratoria = 'n'
temperatura = 10
cansancioEscalofrio = 's'
dolorCabezaGarganta = 's'

usuario = PacienteCovit(documento,nombreCompleto,fechaNacimiento,enfermedadPresion,enfermedadGlicemia,tosSeca,dificultadRespiratoria,temperatura,cansancioEscalofrio,dolorCabezaGarganta)
print(usuario.diagnostico())
print(usuario.tratamiento())
print(usuario.valorConsulta())
usuario.mostrarDatos()
"""

if tosSeca == 's' and dificultadRespiratoria == 's' and temperatura > 37.5 and cansancioEscalofrio == 's' and dolorCabezaGarganta == 's':
    usuario1 = PacienteCovit(documento,nombreCompleto,fechaNacimiento,enfermedadPresion,enfermedadGlicemia,tosSeca,dificultadRespiratoria,temperatura,cansancioEscalofrio,dolorCabezaGarganta)
    usuario1.diagnostico()
    usuario1.tratamiento()
    usuario1.mostrarDatos("Instancia del PacienteCovit #1")    
else:
    usuario1 = PacienteGeneral(documento,nombreCompleto,fechaNacimiento,enfermedadPresion,enfermedadGlicemia,tosSeca,dificultadRespiratoria,temperatura,cansancioEscalofrio,dolorCabezaGarganta)
    usuario1.diagnostico()
    usuario1.tratamiento()
    usuario1.mostrarDatos("Instancia del PacienteGeneral #1")
#isinstance(atributo,clase) #devuelve false o true si existe el atributo en esa clase
    
    
           
