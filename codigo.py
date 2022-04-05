#import networkx as net
#import matplotlib.pyplot as plt

# Leemos las lineas del fichero
#with open("datos/heroes_final.csv", "r") as fichero:
#    lineas = fichero.readlines()

# Creamos un grafo vacío
#red = net.Graph()

# Añadimos las aristas.
#for linea in lineas:
#    heroes = linea.replace("\n", "").split(",")
#    red.add_edge(heroes[0], heroes[1])

# Imprimimos valores como el número de nodos y el número de aristas.
#print("num. nodes: ", len(red.nodes), " num. conexiones: ", len(red.edges))

# Filtramos los usuarios
#limit = 300
#to_remove = []
#for node in red.nodes:
#    grado = red.degree(node)
#    if grado < limit:
#        to_remove.append(node)

#for node in to_remove:
#    red.remove_node(node)


# El siguiente paso es detectar comunidades.
#resultado = net.community.greedy_modularity_communities(red)

#print("NumCommunidades: ", len(resultado))
#color_map = []

#colors = ['red', 'blue', 'yellow', 'green', 'orange']

#for node in red.nodes:
#    com_id = 0
#    for community in resultado:
#        if node in community:
#            color_map.append(colors[com_id])
#        com_id += 1

# Pintamos el grafo resultante
#net.draw(red, node_color=color_map)
#plt.show()
#plt.savefig("Graph.png", format="PNG")

# Ahora trabajamos con una comunidad
#estudiar = resultado[0]

#to_remove = []
#for node in red.nodes:
#    if node not in estudiar:
#        to_remove.append(node)

#for node in to_remove:
#    red.remove_node(node)

#net.draw(red)
#plt.show()

# Pintamos nodos en función de su relevancia
#betweetness = net.betweenness_centrality(red)

#net.draw(red, nodelist=betweetness.keys(), node_size=[v * 150000 for v in betweetness.values()])
#plt.show()
