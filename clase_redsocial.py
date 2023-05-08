# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class redessociales:
    def __init__(self,usuario,correo,amigos,plataforma):
        self.usuario=usuario
        self.correo=correo
        self.amigos=amigos
        self.plataforma=plataforma
        
    def iniciars (self):
        print("bienvenido",self.usuario,"has iniciado sesion en",self.plataforma)
        
    def cerrars(self):
        print("hasta luego",self.usuario,"cerrando sesion.....")
        
    def publicar(self,cosa):
        print("se ha publicado tu",cosa)
        
    def mensaje(self, ami):
        print("has enviado un mensaje a",ami)
        
    def soliami(self,des):
        print("has enviado una solicitud de amistad a",des)
        
p1=redessociales("andy", "12356", 123,"facebook")
p1.iniciars()
p1.mensaje("juan")
p1.publicar("foto")
p1.soliami("maria")
p1.cerrars()