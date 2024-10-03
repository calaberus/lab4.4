class Termostato: 
    def__init__(self,temperatura_inicial):
        self.temperatura= temperatura_inicial
        
    def aumentar_temperatura(self,grados):
        self.temperatura+= grados
    
    def disminuir_(self,grados):
        self.temperatura-= grados 
        
    def mostar_temperatura(self):
        prin(f"la temperatura actual es {self,temperatura}°c.")
