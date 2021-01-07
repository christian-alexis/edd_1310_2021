from colas import Queue,BoundedPriorityQueue
q1 = Queue()
q1.enqueue(3)
q1.enqueue(23)
q1.enqueue(23)
q1.enqueue(53)
q1.dequeue()
print(q1.length())
print(q1.to_string())

print ("prueba 2 de Queue")

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


print("PRUEBAS DE LAS COLAS CON RPIORIDAD ACOTADA")


maestres = {"prioridad":4,"descripcion":"Maestre","personas":["juan p","Diego h"]}
niños ={"prioridad":2,"descripcion":"Niños ","personas":["Santi h","Angel h"]}
mecanicos = {"prioridad":4,"descripcion":"Macanicos","personas":["Diana T","Maria Z"]}

cpa = BoundedPriorityQueue(7)
cpa.enqueue(maestres['prioridad'],maestres)
cpa.enqueue(niños['prioridad'],niños)
cpa.enqueue(mecanicos['prioridad'],maestres)
cpa.to_string()