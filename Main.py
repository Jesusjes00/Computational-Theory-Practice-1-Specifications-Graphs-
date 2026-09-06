
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

        