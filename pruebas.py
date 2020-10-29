from arrays import Array


algo = Array(10)
print(algo.get_item(6363))
print(algo.get_item(3))
print(algo.set_item(555,3))
print(f"el arreglo tiene elementos {algo.get_length()}elementos")
algo.clear(777)
print(algo.get_item(3))
print("aqui empieza el iterador" )
for x in algo:
    print(x)
