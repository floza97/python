from empleado import empleado
from proyecto_persona_hospital.cliente import cliente
from persona import persona




#print(emp,'\n',cli)


def cargar():
    
   
    try:
            
            print('selecciones una opcion: \n' 
                      ' 1- Registrar Empleado \n' 
                      ' 2- Registrar Cliente\n' 
                      ' 3- Salir')
            respuesta = int(input('digite el numero correspondiente '))

            if respuesta == 1 or respuesta == 2:
                nombre = input('ingrese el nombre ')
                apellido = input('ingrese el apellido ')
                edad = input('ingrece la edad ')
                genero = input('ingrece el genero ')

                if respuesta == 1:
                    salario = input('ingrese el salario ')
                    emp = empleado(nombre,apellido,edad,genero,str(salario))
                    personas.append(emp)
                    
                elif respuesta == 2:
                    categoria = input('ingrese la categoria ')
                    cli = cliente(nombre,apellido,edad,genero,categoria)
                    personas.append(cli) 

            elif respuesta == 3:
                print('sesion terminada')
            else:
                print(str(respuesta)+' '+'no es una obcion valida, esta fuera del rango')
                    
    except ValueError:
         print(" *[error de tipeo por favor esriba un numero dentro del rango]* ") 



personas = []
cargar()
print(personas)
'''for persona in personas:
     print(personas)'''



