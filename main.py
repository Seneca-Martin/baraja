import baraja

palos = ['o', 'c', 'e', 'b']
numeros = ['A', '2', '3', '4', '5', '6', '7', 'S', 'C', 'R']

ordenada = baraja.creaBaraja(palos, numeros)
print("Esta es la primera baraja: ",ordenada)

otraBaraja = baraja.creaBaraja(palos, numeros)
print("Esta es la segunda baraja nada más crearla: ", otraBaraja)
baraja.barajar(otraBaraja)
print ("Y ahora la he barajado: ", otraBaraja)
print("Esta es la primera baraja de nuevo: ", ordenada)
