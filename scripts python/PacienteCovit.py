# -*- coding: utf-8 -*-
"""
Created on Thu May  7 22:14:54 2020

@author: leonardo.patino
"""
from Paciente import Paciente

class PacienteCovit(Paciente):
    def __init__(self,documento,nombreCompleto,fechaNacimiento,enfermedadPresion,enfermedadGlicemia,tosSeca,dificultadRespiratoria,temperatura,cansancioEscalofrio,dolorCabezaGarganta):
        #llamar al contructor Paciente
        super().__init__(documento,nombreCompleto,fechaNacimiento,enfermedadPresion,enfermedadGlicemia,tosSeca,dificultadRespiratoria,temperatura,cansancioEscalofrio,dolorCabezaGarganta)
        while True:
            try:
                self.contraseña = input("Ingrese contraseña de 6 digitos: ")
                if len(self.contraseña) == 6:
                    break
                else:
                    print("asegurese de colocar una contraseña de 6 digitos") 
            except Exception as e:
                    print("Error, asegurese de colocar una contraseña válida")
        while True:
            try:
                self.asistenciaRespiratoria = input("Ingrese asistenciaRespiratoria (s:sí/n:no): ")
                if self.asistenciaRespiratoria in ('s','n'):
                    break
                else:
                    print("asegurese de colocar un dificultadRespiratoria válido") 
            except Exception as e:
                    print("Error, asegurese de colocar un dificultadRespiratoria válido")                     
                    
    def diagnostico(self):
        return "Paciente Infectado con COVID-19. Empezar protocolo de salud"
        
    def tratamiento(self):
        if self.hospitalizacion == 's':
            return "Paciente será atendido en el hospital"
        else:
            return "No existe tratamiento o vacuna recomendamos cuidarse en casa"
    
    def __valorConsulta(self):
        if self.hospitalizacion == 's':
            while True:
                try:
                    dias = int(input("Ingrese dias: "))
                    if dias >= 0:
                        break
                    else:
                        print("asegurese de colocar un numero positivo")
                except Exception as e:
                        print("No se permiten letras, asegurese de colocar un numero positivo")            
            valConsulta =  dias * 855000
        else:
            valConsulta = self.salario * 0.002
        return valConsulta    
        
    def mostrarDatos(self,mensaje):
        print(mensaje)
        print(self.diagnostico())
        print(self.tratamiento())
        print("Asistencia Respiratoria: ",self.asistenciaRespiratoria)
        if self.contraseña == '654321':
            print(self.valorConsulta())
        else:
            print("Acceso no permitido")
        

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

