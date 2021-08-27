# Escribe tus funciones abajo de esta línea
def pies_cm (pies):
    centimetros=pies*30.48
    return centimetros
def pulgadas_cm (pulgadas):
    centimetros=pulgadas*2.54
    return centimetros   
def yardas_cm (yardas):
    centimetros=yardas*91.44
    return centimetros    
def main():
    # Escribe tu código abajo de esta línea
    print('1. pies a cm, 2. pulgadas a cm, 3. yardas a cm')
    opcion=int(input('Introduce una opcion: '))
    cantidad=int(input('Introduce la cantidad: '))
    if opcion ==1 :
     respuesta= pies_cm(cantidad)
     print(respuesta)
    elif opcion ==2 :
     respuesta= pulgadas_cm(cantidad)
     print(respuesta) 
    elif opcion ==3 :
     respuesta= yardas_cm(cantidad)
     print(respuesta) 
    else :
     print('Error')    
      



    



if __name__ == '__main__':
    main()
