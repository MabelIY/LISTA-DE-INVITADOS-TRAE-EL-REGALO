'''
Leer nombre de invitados y agregarlos a una lista si han tríado regalo.
Tener la opción de dentener la adición de invitados
Finalmente imprimir los invitados que llevaron regalo.
'''

lista_invitados = []

while True:
  nombre = input("Nombre del invitado: ")
  regalo = input("¿Ha tarido regalo?: ")
  
  if regalo.upper() == "SI":
    lista_invitados.append(nombre)
  elif regalo.upper() == "NO":
    pass

  opcion = input("¿Agregar otro invitado?: ")
  print("\n")
  if opcion.upper() == "SI":
    pass
  elif opcion.upper() == "NO":
    break
    
print(lista_invitados)
