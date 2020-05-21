# -*- coding: utf-8 -*-
"""
Created on Thu May  7 22:15:15 2020

@author: leonardo.patino
"""
from Paciente import Paciente

class PacienteGeneral(Paciente): #en caso de hacer herencia multiple se debe utilizar super() para inicializar los atributos de la super clase (clase que heredamos de primeras)
    def __init__(self,documento,nombreCompleto,fechaNacimiento,enfermedadPresion,enfermedadGlicemia,tosSeca,dificultadRespiratoria,temperatura,cansancioEscalofrio,dolorCabezaGarganta):
        #llamar al contructor Paciente
        super().__init__(documento,nombreCompleto,fechaNacimiento,enfermedadPresion,enfermedadGlicemia,tosSeca,dificultadRespiratoria,temperatura,cansancioEscalofrio,dolorCabezaGarganta)
       
        while True:
            try:
                self.peso = int(input("Ingrese peso: "))
                if self.peso >= 0:
                    break
                else:
                    print("asegurese de colocar un numero positivo")
            except Exception as e:
                    print("No se permiten letras, asegurese de colocar un numero positivo") 
                    
        while True:
            try:
                self.conjuntivitis = input("Tiene conjuntivitis (s:sí/n:no): ")
                if self.conjuntivitis in ('s','n'):
                    break
                else:
                    print("asegurese de colocar un enfermedadPresion válido") 
            except Exception as e:
                    print("Error, asegurese de colocar un enfermedadPresion válido") 
                    
    def diagnostico(self):
        if self.tosSeca == 's' and self.dolorCabezaGarganta == 's' and self.conjuntivitis == 's':
            return "Sarampión"
        elif self.tosSeca == 's' and self.temperatura > 37.5 and self.dificultadRespiratoria == 'n':    
            return "Gripe"
        elif self.tosSeca == 's' and self.temperatura > 37.5 and self.dolorCabezaGarganta == 'n':
            return "Resfriado"
        else:
            return 'Otro'
        
    def tratamiento(self):
        if self.enfermedadPresion == 's' and self.enfermedadGlicemia == 's' and self.edad > 70:
            msg = "Cuidarse porque eres  propenso a contagiarte con COVID-19"
        else:
            msg = ""            
        diagnostico = self.diagnostico()
        if diagnostico == "Sarampión":
            return "Alejarse de las personas. Tomar medicamentos. Llamar al médico si ves complicaciones " + msg
        elif diagnostico == "Gripe":
            return "Evitar bebidas frías. No salir en la noche. Tomar medicamentos " + msg
        elif diagnostico == "Resfriado":
            return "Evitar bebidas frías. Tomar medicamentos. Cubrirse bien si va a salir de casa " + msg
        elif diagnostico == "Otro":
            return "No entendemos porque vino al hospital" + msg
    
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
            
            valConsulta =  dias * 500000
        else:
            valConsulta = self.salario * 0.0015
        return valConsulta 
    
    def mostrarDatos(self,mensaje):
        print(mensaje)
        print("diagnostico: ",self.diagnostico())
        print("tratamiento: ",self.tratamiento())
        print("Peso: ",self.peso)
        print("conjuntivitis: ",self.conjuntivitis)


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

usuario = PacienteGeneral(documento,nombreCompleto,fechaNacimiento,enfermedadPresion,enfermedadGlicemia,tosSeca,dificultadRespiratoria,temperatura,cansancioEscalofrio,dolorCabezaGarganta)
print(usuario.diagnostico())
print(usuario.tratamiento())
print(usuario.valorConsulta())
usuario.mostrarDatos()
"""

    