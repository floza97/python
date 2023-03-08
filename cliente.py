from persona import persona 

class cliente(persona):
    def __init__(self,nombre,apellido, edad, genero, categoria):
       super().__init__(nombre,apellido, edad, genero)
       self.categoria = categoria 

    def __repr__(self):
           return self.nombre +' '+ self.apellido +' '+ self.genero +' '+self.categoria