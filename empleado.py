from persona import persona 

class empleado(persona):
     def __init__(self, nombre,apellido, edad, genero, salario,):
       super().__init__(nombre,apellido, edad, genero)
       self.salario = salario 


     def __repr__(self):
           return self.nombre +' '+ self.apellido +' '+ self.genero +' '+str(self.edad)+' '+str(self.salario)
     