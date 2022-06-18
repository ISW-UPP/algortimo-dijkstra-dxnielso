class Arista:
    def __init__(self, verticeInicial, verticeFinal, peso):
        self.verticeInicial = verticeInicial
        self.verticeFinal = verticeFinal
        self.peso = peso
        
class Camino:
    def __init__(self, aristas, peso):
        self.aristas = aristas
        self.peso = peso

def menu():
    print("\n\tMENÚ")
    print("1. Insertar nodos")
    print("2. Insertar aristas")
    print("3. Mostrar grafo")
    print("4. Mostrar aristas")
    print("5. Mostrar nodos")
    print("6. Dijkstra")
    print("7. Salir")
    
    opcion = int(input("Elige una opción: "))
    return opcion

def dijkstra(origen, destino, arista, aristas):
    caminos = []
    if(len(aristas) != 0):
        for arista in aristas:
            camino = Camino([], 0)
            for aristaRecorrida in aristas:
                if(aristaRecorrida.verticeInicial == origen):
                    camino.aristas.append(aristaRecorrida)
                    camino.peso = camino.peso + aristaRecorrida.peso
                    if(aristaRecorrida.verticeFinal == destino):
                        caminos.append(camino)
                        break
                    else:
                        origen = aristaRecorrida.verticeFinal
                        
        # Buscamos el camino mas corto
        print("espacios de caminos: ", len(caminos))
        menor = caminos[0]
        for camino in caminos:
            if(camino.peso < menor.peso):
                menor = camino
            
        print("CAMINO MAS CORTO")
        print("Acomulado: ", menor.peso)
        print("Iteraciones: ", len(menor.aristas))
        for arista in menor.aristas:
            print(arista.verticeInicial, "->", arista.verticeFinal)
            print("Peso: ", arista.peso)
        # * * * * * * * *
    else:
        print("No hay vertices")
    
    

# Variables globales
opcion = 1
vertices = []
aristas = []

while(opcion != 7):    
    opcion = menu()
    
    if(opcion <= 0 or opcion > 7 ): print("Debes ingresar una opción válida\n\n")
    elif(opcion == 7):
        print("Saliendo...")
    else:
        #Insertar vertices
        if(opcion == 1):
            numVertices = int(input("Ingresa el número de vértices que deseas agregar al grafo: "))
            # por cada vertice que desea agregar va hacer lo siguiente
            for i in range(0, numVertices):
                letraValida = False
                print("\n\tVERTICE ", i+1)
                # while para pedir letra hasta que no se repita
                while(letraValida == False):
                    letra = input("Letra: ")
                    # print("Entro aqui")
                    # for para revisar que la letra no se repita
                    if(len(vertices) != 0):
                        for vertice in vertices:
                            if(letra == vertice):
                                letraValida = False
                                print("Letra repetida, ingresa otra")
                                break
                            else:
                                letraValida = True
                    else:
                        letraValida = True
                vertices.append(letra)

        # Insertar aristas
        elif(opcion == 2):
            existe = False
            letrasExistentes = 0
            verticeUno = input("Vertice inicial: ")
            verticeDos = input("Vertice final: ")
            peso = int(input("Peso: "))
            
            # comprobamos que existan las letras
            if(len(vertices) != 0):
                for vertice in vertices:
                    # pongo los if separados porque despues si ingresaba la letra en la arista inicial y final me daba como resultado en letras existentes solo 1
                    if(vertice == verticeUno):
                        letrasExistentes = letrasExistentes + 1
                    if(vertice == verticeDos):
                        letrasExistentes = letrasExistentes + 1
                
            # si las 2 letras existen
            if(letrasExistentes == 2):
                # compruebo si la arista ya existe
                for arista in aristas:
                    if(arista.verticeInicial == verticeUno and arista.verticeFinal == verticeDos):
                        print("Ya existe esa arista")
                        existe = True
                        break
                # si la arista no existe la agrego
                if(existe == False):
                    aristas.append(Arista(verticeUno, verticeDos, peso))
                    print("La arista se agrego correctamente")
            else:
                print("La(s) letras ingresadas no existen")
                    
        # Mostrar grafo  
        elif(opcion == 3):
            if(len(aristas) != 0):
                for arista in aristas:
                    print("Vértice (", arista.verticeInicial, ") apunta a vértice (", arista.verticeFinal, ")")
            else:
                print("No hay aristas registradas")
                
        # Mostrar aristas
        elif(opcion == 4):
            if(len(aristas) != 0):
                for arista in aristas:
                    print(arista.verticeInicial, " -> ", arista.verticeFinal)
            else:
                print("No hay aristas registradas")
        
        # Mostrar vertices
        elif(opcion == 5):
            if(len(vertices) != 0):
                # for vertice in vertices:
                print("Vertices:",', '.join(vertices))
            else:
                print("No hay vertices")
        
        # Algoritmo Dijkstra
        elif(opcion == 6):
            origen = input("Nodo Origen: ")
            destino = input("Destino: ")     
            existe = False
            letrasExistentes = 0
            
            # comprobamos que existan las letras
            if(len(vertices) != 0):
                for vertice in vertices:
                    # pongo los if separados porque despues si ingresaba la letra en la arista inicial y final me daba como resultado en letras existentes solo 1
                    if(vertice == verticeUno):
                        letrasExistentes = letrasExistentes + 1
                    if(vertice == verticeDos):
                        letrasExistentes = letrasExistentes + 1
                
            # si las 2 letras existen
            if(letrasExistentes == 2):
                dijkstra(origen, destino, arista, aristas)
                        
            else:
                print("La(s) letras ingresadas no existen")