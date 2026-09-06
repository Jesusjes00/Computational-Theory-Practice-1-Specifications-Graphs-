
#global variables
MAX = 20
map_node = {}  #Dictionary to store nodes
count_nodes= 0 #Counter to assign number to the nodes
def createMatrix():
    global MAX
    matrix =[[0 for _ in range(MAX)]for _ in range(MAX)]
    return matrix

def assignnode(name):
    global map_node
    global count_nodes
    if name not in  map_node:
        map_node[name]=count_nodes
        count_nodes +=1
def add_edge(name1,name2,matrix):
    global map_node
    if name1 in map_node and name2 in map_node :
        i = map_node[name1]
        j = map_node[name2]
        matrix[i][j] = 1
        return 0
    else:
        print("No se encontro alguno de los 2 nodos")
        return 1