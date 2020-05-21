# -*- coding: utf-8 -*-
"""
Created on Fri May  8 16:28:51 2020

@author: leonardo.patino
"""

class Credenciales:
    def __init__(self,usuario):
        self.usuario = usuario
        while True:
            try:
                self.contraseña = input("Ingrese contraseña de 6 digitos: ")
                if len(self.contraseña) == 6:
                    break
                else:
                    print("asegurese de colocar una contraseña de 6 digitos") 
            except Exception as e:
                    print("Error, asegurese de colocar una contraseña válida")

    def pintar(self):
        print("Usuario: ",self.usuario)
        print("Contraseña: ",self.contraseña)

class Socialmedia(Credenciales):
    def __init__(self,usuario,facebook,google):
        super().__init__(usuario)
        self.facebook = facebook
        self.google = google
        
    def pintar(self):
        print("facebook: ",self.facebook)
        print("google: ",self.google)

class Externo(Credenciales):
    def __init__(self,usuario,externo):
        super().__init__(usuario)
        self.externo = externo
        
    def pintar(self):
        print("usuario: ",self.usuario)
        print("externo: ",self.externo)      
        print("usuario: ",self.usuario) 
        
    

usuario = 'leo'
facebook = 'leopr@facebook.com'
google = 'leo@google.com'

g = Socialmedia(usuario,facebook,google)
g.pintar()   

externo = 'leoexterno'
u = Externo(usuario,externo)
u.pintar()      
                    