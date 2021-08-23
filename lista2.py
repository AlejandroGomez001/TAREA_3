import os 
class Lista():
    def __init__(self):
        self.lista=[]
    def insertar(self):
        self.lista=[]
        num1=int(input("Ingrese la cantidad de numeros que desea ingresar en la lista: "))
        c=0
        while c<num1:
           dato=int(input("Ingrese un numero: "))
           self.lista.append(dato)
           c+=1
        print(self.lista)
        return self.lista
    
    def insertarmasdatos (self):
        self.lista=self.insertar()
        elemento=int(input("Ingrese el elemento que desea ingresar en la lista: "))
        self.lista.extend([elemento])
        print(self.lista)
        return [self.lista]

    def buscarelemento (self):
        self.lista=self.insertar()
        s=1
        elemento=int(input("Ingrese el elemento a buscar en la lista: "))
        if (elemento in self.lista):
            s=self.lista.index(elemento)
        print("El indice del elemento ",elemento, " que busco en la lista es: ",s)
        print(self.lista)
        return [self.lista]

    def eliminarElemento (self):
        self.lista=self.insertar()
        elemento=int(input("Ingrese el elemento a remover de la lista: "))
        self.lista.remove(elemento)
        print(self.lista)
        return [self.lista]
        
lista1=Lista()

class Pila:
    def __init__(self,tamanio):
        self.lista=[]
        self.size=tamanio
        self.top=0
    
    def push(self):
        tama=int(input("Ingrese el numero de datos que desea ingresar a la pila: "))
        while self.top < tama:
            dato=int(input("Ingrese un dato: "))
            self.lista= self.lista + [dato]
            self.top += 1
        else:
            print("La lista se encuentra llena a continuacion se mostrara la pila creada")
            
    
    def pop(self):
        if self.empty():
            return None
        else:
            top = self.lista[-1]
            self.lista = self.lista[-1]
            self.top -= 1
            return top
   
    def show(self):
        for top in range(self.top -1,-1,-1):
            print ("[{}]".format(self.lista[top]))
    
    def longitud(self):
        return self.top      
       
    def show(self):
        for top in range(self.top -1,-1,-1):
            print ("[{}]".format(self.lista[top]))
    
    def empty(self):
        if self.top == 0:
            return True
        else:
            return False
pila1 = Pila(5)
class Cola:
    def __init__(self):
        self.cola=[]

    def agregar(self):
        ing=int(input("Ingrese el numero de datos que desea agregar a su cola: "))
        c=0
        while c<ing:
            dato=int(input("Ingrese el numero a ingresar: "))
            c+=1
            self.cola.append(dato)
        print(self.cola)
        
cola1=Cola()
class Menu:
    def __init__(self,titulo,opciones=[]):
        self.titulo =titulo
        self.opciones=opciones
    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc=input("Elija Opcion[1...{}]: ".format(len(self.opciones)))
        return opc
opc="0"
while opc!="4":
  os.system("cls")
  men=Menu("Menu Principal", ["1) Lista", "2) Pila","3) Cola","4) Salir"])
  opc=men.menu()
  if opc=="1":
      opc1="0"
      os.system("cls")
      while opc1!="4":
          men1=Menu("Menu Lista",["1) Buscar Elemento en lista","2) Eliminar Elemento en Lista", "3) Insertar Elemento en Lista", "4) Salir"])
          opc1=men1.menu()
          os.system("cls")
          if opc1=="1":
              print("Buscar Elemento en lista")
              lista1.buscarelemento()
              input("Presione una tecla para continuar...")
              os.system("cls")
          elif opc1=="2":
              os.system("cls")
              print("Eliminar Elemento en lista")
              lista1.eliminarElemento()
              input("Presione una tecla para continuar...")
              os.system("cls")
          elif opc1=="3":
              os.system("cls")
              print("Insertar Elemento en Lista")
              lista1.insertarmasdatos()
              input("Presione una tecla para continuar...")
              os.system("cls")
          elif opc1=="4":
              os.system("cls")
              print("Gracias por usar lista")
              
  elif opc=="2":
      opc2="0"
      os.system("cls")

      while opc2!="2":
          men2=Menu("Menu Pila",["1) Insertar datos a la pila", "2) Salir"])
          opc2=men2.menu()
          os.system("cls")
          if opc2=="1":
              print("Insertar datos a la pila")
              pila1.push()
              pila1.show()
              input("Presione una tecla para continuar...")
              os.system("cls")
          elif opc2=="2":
              os.system("cls")
              print("Gracias por usar pila")
  elif opc=="3":
        opc3="0"
        os.system("cls")

        while opc3!="2":
          men2=Menu("Menu cola",["1) Insertar nuevo dato a la cola", "2)Salir"])
          opc3=men2.menu()
          os.system("cls")
          if opc3=="1":
              print("Insertar nuevo dato a la cola")
              cola1.agregar()
              input("Presione una tecla para continuar...")
              os.system("cls") 
          elif opc3=="2":
              os.system("cls")
              print("Gracias por usar cola")
  elif opc=="4":
        print("Gracias por usar el sistema")
  else:
        print("Opcion no valida")

print("Algoritmo finalizado")