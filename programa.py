import os
import string
import logging
from time import sleep

def clear():
  # for windows
  if os.name == 'nt':
    _ = os.system('cls')
   # for mac and linux
  else:
    _ = os.system('clear')

logging.basicConfig(filename='accionesResultados.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
print("Bienvenido al gestor de textos en pila")
logging.info("Inicio de ejecución del programa")
if not os.path.exists('pila.txt'):
  f = open('pila.txt', 'x')
  f.close()
while True:
  print("Seleccione dentro de las opciones:")
  print("1. Ingresar texto a la pila")
  print("2. Quitar texto de pila")
  print("3. Buscar el texto más largo y el más corto")
  print("4. Imprimir texto de pila")
  print("5. Comparar tamaños de textos en la pila")
  print("6. Salir")
  opcion = int(input("Opción: "))
  if opcion == 1:
    fr = open('pila.txt', 'r')
    lista = fr.read()
    fr.close()
    numPalabras = len(lista.strip().split())
    if(numPalabras<20):
      f = open('pila.txt', 'a')
      if 20-numPalabras == 1:
        inputuser = input("Ingrese el texto para la pila. Puedes ingresar solo "+str(20-numPalabras)+" texto (sin ninguna puntuacion):")
      else:
        inputuser = input("Ingrese el texto para la pila. Puedes ingresar hasta "+str(20-numPalabras)+" textos (sin ninguna puntuacion) separados por espacio:")
      textos = inputuser.split()
      textos = textos[:(20-len(lista.strip().split()))]
      for i in range(len(textos)):
        textos[i] = textos[i].translate(str.maketrans('','',string.punctuation))
        textos[i] = textos[i][:100]
        f.write(textos[i]+' ')
      f.close()
      clear()
      if len(textos) == 1:
          logging.info('Se ingreso '+str(len(textos))+' texto a la pila.')
      else:
          logging.info('Se ingresaron '+str(len(textos))+' textos a la pila.')
      clear()
    else:
      clear()
      logging.warning('Pila llena. No se pueden ingresar más textos.')
      clear()
  elif opcion == 2:
    with open('pila.txt', 'r+') as file:
      lista = file.read()
    lista = lista.strip().split()
    if len(lista) != 0:
      lista.pop(-1)
      f = open('pila.txt', "w")
      for i in range(len(lista)):
        f.write(lista[i]+' ')
      f.close()
      clear()
      print("Último elemento de la pila eliminado")
      logging.info('Último elemento de la pila removido (pop).')
      sleep(1)
      clear()      
    else:
      clear()
      print("Pila vacía. No hay textos para eliminar")
      logging.warning('Pila vacía. No hay textos para eliminar.')
      sleep(2)
      clear()
  elif opcion == 3:
    f = open('pila.txt', 'r')
    lista = f.read()
    f.close()
    lista = lista.strip().split()
    if len(lista) != 0:
      largoMax = 0
      largoMin = 101
      indiceMax = -1
      indiceMin = -1
      for i in range(len(lista)):
        if len(lista[i])>largoMax:
          largoMax = len(lista[i])
          indiceMax = i
        if len(lista[i])<largoMin:
          largoMin = len(lista[i])
          indiceMin = i
      if largoMax != largoMin:
        clear()
        if largoMax == 1:
          print("El texto más largo de la pila es \""+lista[indiceMax]+"\" con", largoMax, "caracter")
        elif largoMax > 1:
          print("El texto más largo de la pila es \""+lista[indiceMax]+"\" con", largoMax, "caracteres")
        if largoMin == 1:
          print("El texto más corto de la pila es \""+lista[indiceMin]+"\" con", largoMin, "caracter")
        elif largoMin > 1:
          print("El texto más corto de la pila es \""+lista[indiceMin]+"\" con", largoMin, "caracteres")
        logging.info('Se mostraron dos textos de longitud máxima y mínima.')
        sleep(4)
        clear()
      else:
        clear()
        if indiceMax == indiceMin:
          if len(lista) == 1:
            print("La pila solamente contiene un texto, por lo que \""+lista[indiceMax]+"\" es el texto más largo y más corto simultaneamente.")
            logging.info('Se mostró solamente un texto que resulta ser el texto más corto y el más largo a la vez.')
            sleep(3)
            clear()
          else:
            print("La pila contiene textos de un solo tamaño. Así, una de estas palabras es \""+lista[indiceMax]+"\".")
            logging.info('Se mostró solamente un texto que resulta ser el texto más corto y el más largo a la vez.')
            sleep(3)
            clear()
        else:
          if largoMax == 1:
            print("Dentro de la pila, el texto mas largo y el mas corto tienen", largoMax, "caracter, dentro de los cuales, uno de ellos es la palabra \""+lista[indiceMax]+"\"")
          elif largoMax > 1:
            print("Dentro de la pila, el texto mas largo y el mas corto tienen", largoMax, "caracteres, dentro de los cuales, uno de ellos es la palabra \""+lista[indiceMax]+"\"")
          logging.info('En la pila se encuentran solo palabras de un único número de caracteres, por lo que se mostró el primer resultado.')
          sleep(4)
          clear()
    else:
      clear()
      logging.warning('Pila vacía. No hay texto de menor ni de mayor tamaño.')
  elif opcion == 4:
    f = open('pila.txt', 'r')
    lista = f.read()
    listaSep = lista.strip().split()
    f.close()
    clear()
    if len(listaSep) == 0:
      logging.warning('Pila vacía. No hay textos para imprimir.')
      print("La pila se encuentra vacía. Intenta ingresar algunos elementos")
      sleep(2)
      clear()
    elif len(listaSep) == 1:
      print("El único texto que se encuentra en la pila es: \""+listaSep[0]+"\"")
      logging.info('Se imprime el único elemento de la pila.')
      sleep(3)
      clear()
    else:
      while True:
        tipoImp = input("¿Deseas una impresión total o parcial? (T/P)? ")
        if tipoImp == 'T' or tipoImp == "t":
          logging.info('Se imprime la totalidad de la pila.')
          print("El texto que hay en la pila es: \""+lista.strip()+"\"")
          sleep(3)
          clear()
          break
        elif tipoImp == 'P' or tipoImp == "p":
          while True:
            posicion = int(input("Escoge la posición del texto que quieres imprimir. Tienes para escoger entre 1 y "+str(len(listaSep))+": "))
            if posicion not in list(range(1,len(listaSep)+1)):
              print("Ingresa un valor válido")
              logging.warning('Se ingresa un índice de impresión inválido')
              sleep(1)
              clear()
            else:
              break
          print("El texto que se encuentra en la posición", posicion, "de la pila es: \""+listaSep[posicion-1]+"\"")
          logging.info('Se imprime el elemento '+str(posicion)+' de la pila')
          sleep(3)
          clear()
          break
        else:
          clear()
          print("Debes ingresar una opción válida para el tipo de impresión")
          logging.warning('Tipo de impresión solicitado no válido.')
          sleep(2)
          clear()
  elif opcion == 5:
    f = open('pila.txt', 'r')
    lista = f.read()
    listaSep = lista.strip().split()
    f.close()
    clear()
    if len(listaSep) == 0:
      clear()
      print("La pila se encuentra vacía. No hay textos para comparar.")
      logging.warning('Pila vacía. No hay textos para comparar.')
      sleep(2)
      clear()
    elif len(listaSep) == 1:
      clear()
      print("La pila contiene solo al texto \""+listaSep[0]+"\" por lo que no tiene comparación dentro de la pila.")
      logging.info('Pila con un solo elemento. No se efectúa comparación.')
      sleep(2)
      clear()
    else:
      print("Ingresa las posiciones de los dos textos a comparar (entre 1 y "+str(len(listaSep))+")")
      while True:
        pos1 = int(input("Posición 1: "))
        if pos1 not in list(range(1,len(listaSep)+1)):
          print("Ingresa una posición válida")
          logging.warning('Posición 1 inválida')
        else:
          break
      while True:
        pos2 = int(input("Posición 2: "))
        if pos2 not in list(range(1,len(listaSep)+1)):
          print("Ingresa una posición válida")
          logging.warning('Posición 2 inválida')
        else:
          break
      texto1 = listaSep[pos1 - 1]
      texto2 = listaSep[pos2 - 1]
      if len(texto1) > len(texto2):
          if len(texto1)-len(texto2) == 1:
              print("El texto "+str(pos1)+": \""+texto1+"\" es mayor en tamaño que el texto "+str(pos2)+": \""+texto2+"\" en "+str(len(texto1)-len(texto2))+" caracter.")
          else:
              print("El texto "+str(pos1)+": \""+texto1+"\" es mayor en tamaño que el texto "+str(pos2)+": \""+texto2+"\" en "+str(len(texto1)-len(texto2))+" caracteres.")
          logging.info("Entrada 1: \""+texto1+"\", Entrada 2: \""+texto2+"\", resultado: Pos1 > Pos2.")
      elif len(texto2) > len(texto1):
          if len(texto2)-len(texto1) == 1:
              print("El texto "+str(pos2)+": \""+texto2+"\" es mayor en tamaño que el texto "+str(pos1)+": \""+texto1+"\" en "+str(len(texto2)-len(texto1))+" caracter.")
          else:
              print("El texto "+str(pos2)+": \""+texto2+"\" es mayor en tamaño que el texto "+str(pos1)+": \""+texto1+"\" en "+str(len(texto2)-len(texto1))+" caracteres.") 
          logging.info("Entrada 1: \""+texto1+"\", Entrada 2: \""+texto2+"\", resultado: Pos2 > Pos1.")
      elif len(texto1) == len(texto2):
        print("El texto "+str(pos1)+": \""+texto1+"\" es igual en tamaño que el texto "+str(pos2)+": \""+texto2+"\"")
        logging.info("Entrada 1: \""+texto1+"\", Entrada 2: \""+texto2+"\", resultado: Pos2 = Pos1.")
      sleep(4)
      clear()
  elif opcion == 6:
    logging.info("Término de ejecución del programa")
    break
  else:
    clear()
    print("Ingresa una opción válida.")
    logging.warning("Opción de interfaz inválida")
    sleep(1)
    clear()
