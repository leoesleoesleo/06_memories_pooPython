# -*- coding: utf-8 -*-

class Paciente:
    def __init__(self,documento,nombreCompleto,fechaNacimiento,enfermedadPresion,enfermedadGlicemia,tosSeca,dificultadRespiratoria,temperatura,cansancioEscalofrio,dolorCabezaGarganta):
        self.documento = documento
        self.nombreCompleto = nombreCompleto
        self.fechaNacimiento = fechaNacimiento
        
        while True:
            try:
                self.edad = int(input("Ingrese edad: "))
                if self.edad >= 0:
                    break
                else:
                    print("asegurese de colocar un numero positivo")
            except Exception as e:
                    print("No se permiten letras, asegurese de colocar un numero positivo")   
            
        self.enfermedadPresion = enfermedadPresion
        self.enfermedadGlicemia = enfermedadGlicemia
        self.tosSeca = tosSeca
        self.dificultadRespiratoria = dificultadRespiratoria
        self.temperatura = temperatura
        self.cansancioEscalofrio = cansancioEscalofrio
        self.dolorCabezaGarganta = dolorCabezaGarganta
        
        while True:
            try:
                self.hospitalizacion = input("Requiere hospitalización (s:sí/n:no): ")
                if self.hospitalizacion in ('s','n'):
                    break
                else:
                    print("asegurese de colocar un valor válido") 
            except Exception as e:
                    print("Error, asegurese de colocar un valor válido") 
                    
        while True:
            try:
                self.salario = int(input("Ingrese salario: "))
                if self.salario >= 0:
                    break
                else:
                    print("asegurese de colocar un numero positivo")
            except Exception as e:
                    print("No se permiten letras, asegurese de colocar un numero positivo") 
        
    def mostrarEdad(self):
        return self.edad
        
    def mostrarDatos(self,mensaje):
        print(mensaje)
        print("Documento: ",self.documento)
        print("nombreCompleto: ",self.nombreCompleto)
        print("fechaNacimiento: ",self.fechaNacimiento)
        print("edad: ",self.edad)
        print("Tiene enfermedad Presion: ",self.enfermedadPresion)
        print("Tiene enfermedad Glicemia: ",self.enfermedadGlicemia)
        print("Tiene tos Seca: ",self.tosSeca)
        print("Tiene dificultad Respiratoria: ",self.dificultadRespiratoria)
        print("Temperatura: ",self.temperatura)
        print("Tiene cansancio Escalofrio: ",self.cansancioEscalofrio)            
        print("Tiene dolor CabezaGarganta: ",self.dolorCabezaGarganta)
        print("salario: ",self.salario)

            
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

usuario = Paciente(documento,nombreCompleto,fechaNacimiento,enfermedadPresion,enfermedadGlicemia,tosSeca,dificultadRespiratoria,temperatura,cansancioEscalofrio,dolorCabezaGarganta)
usuario.mostrarDatos()
"""