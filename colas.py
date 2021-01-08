#PRUEBAS DE LAS COLAS 
class Queue:
    def __init__(self):
        self.__data = list()

    def is_empty (self):
        return len(self.__data)==0

    def length(self):
        return len(self.__data)

    def enqueue(self,elem):
        self.__data.append(elem)
    
    def dequeue (self):
        if not self.is_empty():
            return self.__data.pop(0) 
        else:
            return None
    def to_string (self):
        cadena = ""
        for elem in self.__data:
            cadena = cadena + "|" + str(elem)
        cadena = cadena +"|"
        return cadena 

#PRUEBAS DE LAS COLAS CON PRIORIDAD NO ACOTADA

class PriorityQueue:
    """
        This priority queue uses a given number as priority order.
        The smallest number has the higher priority
    """
    def __init__(self):
        self.__data = list()

    def is_empty (self):
        return len(self.__data)==0

    def length(self):
        return len(self.__data)

    def enqueue(self, value: str, priority: int) -> None:
        """Add the value the queue based on its priority"""
        self.__data.append((value, priority))
        self.__data = reorder_queue(self.__data)

    def dequeue (self):
        if not self.is_empty():
            return self.__data.pop(0) 
        else:
            return None

    
    def to_string (self):
        cadena = ""
        for elem in self.__data:
            cadena = cadena + "|" + str(elem)
        cadena = cadena +"|"
        return cadena

def reorder_queue(queue):
    return sorted(queue, key=lambda v: v[1])


#PRUEBAS DE LAS COLAS CON PRIORIDAD ACOTADA
class BoundedPriorityQueue:
    def __init__( self , niveles):
        self.__data=[Queue() for x in range(niveles) ]
        self.__size=0

    def is_empty(self):
        return self.__size == 0

    def length(self):
        return self.__size

    def enqueue(self,prioridad,elem):
        if prioridad < len(self.__data) and prioridad >= 0:
            self.__data[prioridad].enqueue(elem)
            self.__size +=1
        
    
    def dequeue (self):
        if not self.is_empty():
            for nivel in self.__data:
                if not nivel.is_empty():
                    self.__size -=1
                    return nivel.dequeue()
            
    def to_string (self):
        if not self.is_empty():
            for nivel in range (len(self.__data)):
                print(f"Nivel {nivel}-->{ self.__data[nivel].to_string()}")
            print("-------------------------------------------------------")
        else: 
            print("\n************** EL BARCO FUE ABANDONADO **************\n")
        
            

        


        




    



            
       


