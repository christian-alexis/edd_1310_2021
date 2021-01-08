from colas import Queue,BoundedPriorityQueue,PriorityQueue
q1 = Queue()
q1.enqueue(3)
q1.enqueue(23)
q1.enqueue(23)
q1.enqueue(53)
q1.dequeue()
print(q1.length())
print(q1.to_string())

print ("\nprueba 2 de Queue\n")

c1={"id":1 , "nombre":"Mario", "balance":20.5}
c2={"id":2 , "nombre":"Diana", "balance":3456.5}
c3={"id":3 , "nombre":"Bartolo", "balance":100000.0}

atencion = Queue()
atencion.enqueue(c1)
atencion.enqueue(c2)
atencion.enqueue(c3)

print(atencion.to_string())
siguiente = atencion.dequeue()
print(f"Bienvenido sr. {siguiente['nombre']}, en que podemos servirle el dia de hoy")
print(atencion.to_string())
print("--------------------------------------------------")

print("\nPRUEBAS DE LAS COLAS CON PRIORIDAD NO ACOTADA\n")
barco = PriorityQueue()
barco.enqueue("Maestre", 4)
barco.enqueue("Niños", 2)
barco.enqueue("Mecanico", 4)
barco.enqueue("Hombres", 3)
barco.enqueue("Vigia", 4)
barco.enqueue("capitan", 5)
barco.enqueue("Timonel", 4)
barco.enqueue("Mujeres", 3)
barco.enqueue("3ra edad ", 2)
barco.enqueue("Niñas", 1)
print(barco.length())
print(barco.to_string())

print("--------------------------------------------------")

print("\nPRUEBAS DE LAS COLAS CON PRIORIDAD ACOTADA\n")


maestres = {"prioridad":4,"descripcion":"Maestre","personas":["juan p","Diego h"]}
niños ={"prioridad":2,"descripcion":"Niños ","personas":["Santi h","Angel h"]}
mecanicos = {"prioridad":4,"descripcion":"Macanicos","personas":["Diana T","Maria Z"]}
hombres = {"prioridad":3,"descripcion":"Maestre","personas":["Pedro p","alberto"]}
vigia ={"prioridad":4,"descripcion":"Niños ","personas":["Mateo h","Eusebio"]}
capitan = {"prioridad":5,"descripcion":"Macanicos","personas":["Dian T","Matilda T"]}
timonel = {"prioridad":4,"descripcion":"Maestre","personas":["Rodrigo y","Dorian h"]}
mujeres ={"prioridad":3,"descripcion":"Niños ","personas":["Elizabeth J","Fny l"]}
tercera_edad = {"prioridad":2,"descripcion":"Macanicos","personas":["Julio T","Alvaro Z"]}
niñas = {"prioridad":1,"descripcion":"Maestre","personas":["Karen p","Donaji Q"]}


cpa = BoundedPriorityQueue(7)
cpa.enqueue(maestres['prioridad'],maestres)
cpa.enqueue(niños['prioridad'],niños)
cpa.enqueue(mecanicos['prioridad'],mecanicos)
cpa.enqueue(hombres['prioridad'],hombres)
cpa.enqueue(vigia['prioridad'],vigia)
cpa.enqueue(capitan['prioridad'],capitan)
cpa.enqueue(timonel['prioridad'],timonel)
cpa.enqueue(mujeres['prioridad'],mujeres)
cpa.enqueue(tercera_edad['prioridad'],tercera_edad)
cpa.enqueue(niñas['prioridad'],niñas)
cpa.to_string()
cpa.dequeue()
cpa.to_string()
cpa.dequeue()
cpa.to_string()
cpa.dequeue()
cpa.to_string()
cpa.dequeue()
cpa.to_string()
cpa.dequeue()
cpa.to_string()
cpa.dequeue()
cpa.dequeue()
cpa.to_string()
cpa.dequeue()
cpa.to_string()
cpa.dequeue()
cpa.to_string()
cpa.dequeue()
cpa.to_string()