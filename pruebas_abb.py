from arboles_binarios import BinarySearchTree

abb= BinarySearchTree()
abb.insert(50)
abb.insert(30)
abb.insert(60)
abb.insert(35)
abb.insert(89)
abb.insert(70)

abb.tranversal()
abb.tranversal("preorden")
abb.tranversal("posorden")
res= abb.search(25)
print(f"el resultado es: {res}")
abb.remove(35)
abb.tranversal()