import random


class hospital:
    def __init__(self):
        nombre= 'upd'
        self.listaPacientes=[]
        
    def ingresarPaciente(self,paciente):
        self.listaPacientes.append(paciente)
        print('Paciente ingresado con exito')
   
    
    def atenderPaciente(self):
        paciente=self.listaPacientes[0]
        self.listaPacientes.pop(0)
        return paciente
    def bucarPacientes(self,documento):
        for i in self.listaPacientes:
            if i.documento == documento:
                print('su turno es :',i.turno)
                return
        print('paciente no existe con ese documento ')
        return 
        
class paciente:
    def __init__(self,nombre,documento,turno):
        self.nombre=nombre
        self.documento=documento
        self.turno=turno
        
upd=hospital()
turno=0
machete=1


while True:
    sala=random.randint(1, 10)
    opt = input('''Ingresa :
1. Para agregar paciente
2. Para antender paciente
3. verificar turno pacientes por cedula ''')

    if opt == '1':
        if machete == 1:
            lst=[]
            plantilla=['nombre','documento']
            for i in plantilla:
                lst.append(input("Ingresa : "+ i +" "))   
            pc=paciente(lst[0],lst[1],'turno '+str(turno))
            upd.ingresarPaciente(pc)
            turno +=1
            if turno == 9:
                turno = 0
            machete=2
        else:
            if len(upd.listaPacientes) == 10:
                print('maxima capacidad de pacientes en espera ')
            else: 
                lst=[]
                plantilla=['nombre','documento']
                for i in plantilla:
                    lst.append(input("Ingresa : "+ i +" "))   
                pc=paciente(lst[0],lst[1],'turno '+str(turno))
                upd.ingresarPaciente(pc)
                turno +=1
                if turno == 9:
                    turno = 0
            
    if opt == '2':
        pc =upd.atenderPaciente()
        print(pc.turno ,' paciente ',pc.nombre ,'favor ingresar a la sala ',sala)
    if opt =='3':
        pd=input('ingresa documento del paciente a buscar ')
        upd.bucarPacientes(pd)