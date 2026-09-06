
#global variables
MAX = 20
map_node = {}  #Dictionary to store nodes
count_nodes= 0 #Counter to assign number to the nodes
start_node = None
end_node = None
matrix = [[0 for _ in range(MAX)] for _ in range(MAX)]


#function to assign nodes
def assignnode(name):
    global map_node
    global count_nodes
    if name not in  map_node:
        map_node[name]=count_nodes
        count_nodes +=1

#function to add edges
def add_edge(name1,name2):
    global map_node
    global matrix
    if name1 in map_node and name2 in map_node :
        i = map_node[name1]
        j = map_node[name2]
        matrix[i][j] = 1
        return 0
    else:
        print("the node doesn´t exist")
        return 1

def setpoints(start_name,end_name):
    global map_node ,start_node,end_node
    #if the node doesn´t exist
    if start_name in map_node and end_name in map_node:
        start_node=map_node[start_name]
        end_node = map_node[end_name]
        return 0
    else:
        print("the node doesn´t exist")
        return 1
