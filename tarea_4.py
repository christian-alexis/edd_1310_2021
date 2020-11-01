class Array:

    
    def __init__(self,tam):
        self.__arreglo=[]

    def leer(self):
        archivo = open("archivo.txt","r")
        for linea in archivo.readlines():
               for linea1 in linea.split(","):
                   self.__arreglo.append(linea1)

           
            
                   
       

    

    def get_item(self , posicion):
        dato = 0
        try:
            dato= self.__arreglo[posicion]
        except Exception as e:
            print("Error de posicion")

        return dato

    def set_item(self ,dato, posicion):
            try:
                self.__arreglo[posicion]= dato
            except Exception as e:
                print("Error de posicion")

            return dato


class Arreglo():

    arreglo=[]

    def __init__(self):
        pass

    def leer1(self):
        archivo = open("archivo.txt","r")


        for row in archivo:
            self.arreglo.append(row)

    def imprimir1(self):
        for row in self.arreglo:
            print(row)


    
objeto1 = Arreglo()

objeto1.leer1()
objeto1.imprimir1()




objeto = Array(14)

objeto.leer()


print("\n++++++++++++++++++++++++++++++++++++++++++++")
print("\nLOS SUELDOS TOTALES DE LOS TRABAJADORES (TOMANDO EN CUENTA HORAS EXTRA Y ANTIGUEDAD) SON:\n")

print(f"El sueldo de {objeto.get_item(8)} {objeto.get_item(9)} {objeto.get_item(10)} es: {float (objeto.get_item(11)) *276.5 +float (objeto.get_item(12)) * 0.3 * 3 + float (objeto.get_item(12)) } $") 

print(f"El sueldo de {objeto.get_item(15)} {objeto.get_item(16)} {objeto.get_item(17)} es: {float (objeto.get_item(18)) *276.5 + float (objeto.get_item(19)) * 0.3 * 0 + float (objeto.get_item(19)) } $") 

print(f"El sueldo de {objeto.get_item(22)} {objeto.get_item(23)} {objeto.get_item(24)} es: {float (objeto.get_item(25)) *276.5 + float (objeto.get_item(26)) * 0.3 * 4 + float (objeto.get_item(26)) } $") 

print(f"El sueldo de {objeto.get_item(29)} {objeto.get_item(30)} {objeto.get_item(31)} es: {float (objeto.get_item(32)) *276.5 + float (objeto.get_item(33)) * 0.3 * 3 + float (objeto.get_item(33)) } $")

print(f"El sueldo de {objeto.get_item(36)} {objeto.get_item(37)} {objeto.get_item(38)} es: {float (objeto.get_item(39)) *276.5 + float (objeto.get_item(40)) * 0.3 * 3 + float (objeto.get_item(40)) } $") 

print(f"El sueldo de {objeto.get_item(43)} {objeto.get_item(44)} {objeto.get_item(45)} es: {float (objeto.get_item(46)) *276.5 +float (objeto.get_item(47)) * 0.3 * 2 + float (objeto.get_item(47)) } $") 

print(f"El sueldo de {objeto.get_item(50)} {objeto.get_item(51)} {objeto.get_item(52)} es: {float (objeto.get_item(53)) *276.5 + float (objeto.get_item(54)) * 0.3 * 2 + float (objeto.get_item(54)) } $") 

print(f"El sueldo de {objeto.get_item(57)} {objeto.get_item(58)} {objeto.get_item(59)} es: {float (objeto.get_item(60)) *276.5 + float (objeto.get_item(61)) * 0.3 * 2 + float (objeto.get_item(61)) } $") 

print(f"El sueldo de {objeto.get_item(64)} {objeto.get_item(65)} {objeto.get_item(66)} es: {float (objeto.get_item(67)) *276.5 + float (objeto.get_item(68)) * 0.3 * 3 + float (objeto.get_item(68)) } $")

print(f"El sueldo de {objeto.get_item(71)} {objeto.get_item(72)} {objeto.get_item(73)} es: {float (objeto.get_item(74)) *276.5 + float (objeto.get_item(75)) * 0.3 * 3 + float (objeto.get_item(75)) } $")

print(f"El sueldo de {objeto.get_item(78)} {objeto.get_item(79)} {objeto.get_item(80)} es: {float (objeto.get_item(81)) *276.5 +float (objeto.get_item(82)) * 0.3 * 1 + float (objeto.get_item(82)) } $") 

print(f"El sueldo de {objeto.get_item(85)} {objeto.get_item(86)} {objeto.get_item(87)} es: {float (objeto.get_item(88)) *276.5 + float (objeto.get_item(89)) * 0.3 * 1 + float (objeto.get_item(89)) } $") 

print(f"El sueldo de {objeto.get_item(92)} {objeto.get_item(93)} {objeto.get_item(94)} es: {float (objeto.get_item(95)) *276.5 + float (objeto.get_item(96)) * 0.3 * 0 + float (objeto.get_item(96)) } $") 

print(f"El sueldo de {objeto.get_item(99)} {objeto.get_item(100)} {objeto.get_item(101)} es: {float (objeto.get_item(102)) *276.5 + float (objeto.get_item(103)) * 0.3 * 4 + float (objeto.get_item(103)) } $")

print("\n++++++++++++++++++++++++++++++++++++++++++++")
print("\nLos trabadores con mayor antiguedad son:")

print(f"\n{objeto.get_item(99)} {objeto.get_item(100)} {objeto.get_item(101)} y {objeto.get_item(22)} {objeto.get_item(23)} {objeto.get_item(24)} ")
print("\nLos trabajadores con menor antiguiedad son:")

print(f"\n{objeto.get_item(15)} {objeto.get_item(16)} {objeto.get_item(17)} y {objeto.get_item(92)} {objeto.get_item(93)} {objeto.get_item(94)}")