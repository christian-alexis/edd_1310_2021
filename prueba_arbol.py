class NodoArbol:
    def __init__ (self, value , left=None , right=None):
        self.data=value
        self.left=left
        self.right=right

arbol = NodoArbol("R",NodoArbol("C"),NodoArbol("H"))
print(arbol.left.data) # Se imprime el valor izquierdo del arbol osea "C" 
print(arbol.data) # Se imprime el valor del arbol que seria "R"
print(arbol.right.data)# Se imprime el valor derecho del arbol osea "H"


arbol2 = NodoArbol(4,  NodoArbol(3,  NodoArbol(2,  NodoArbol(2))) ,  NodoArbol(5))
print(arbol2.data)
print(arbol2.left.data)
print(arbol2.right.data)
print(arbol2.left.left.data)
print(arbol2.left.left.left.data)