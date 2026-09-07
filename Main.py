# global variables
MAX = 20 # Maximum number of nodes
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
        print("the node doesn't exist")
        return 1

def setpoints(start_name,end_name):
    global map_node ,start_node,end_node
    #if the node doesn't exist
    if start_name in map_node and end_name in map_node:
        start_node=map_node[start_name]
        end_node = map_node[end_name]
        return 0
    else:
        print("the node doesn't exist")
        return 1


# DFS ALGORITHM - FIND ALL ROUTES
visited = [False for _ in range(MAX)]  # Cycle control mechanism
all_routes = []  # Stores all found routes
current_route = []  # Current route being explored


def find_all_routes():
    """
    Finds all routes from start_node to end_node using recursive DFS
    with cycle control mechanism (visited array)
    """
    global visited, all_routes, current_route
    
    if start_node is None or end_node is None:
        print("Error: Start or end node are not defined")
        return []
    
    # Reset variables
    visited = [False for _ in range(MAX)]
    all_routes = []
    current_route = []
    
    print(f"\n=== FINDING ROUTES FROM {get_node_name(start_node)} TO {get_node_name(end_node)} ===")
    print("-" * 60)
    
    # Start recursive DFS
    dfs_recursive(start_node)
    
    # Display results
    display_results()
    
    return all_routes


def dfs_recursive(node_index):
    """
    Recursive DFS function with cycle control mechanism
    Uses 'visited' array to prevent infinite loops
    """
    global visited, current_route, all_routes
    
    node_name = get_node_name(node_index)
    
    # Mark current node as visited and add to current route
    visited[node_index] = True
    current_route.append(node_name)
    
    # print nodes as they are being visited
    print(f"Visiting: {node_name} (Current route: {' -> '.join(current_route)})")
    
    # Check if we have reached the end node
    if node_index == end_node:
        # Save a copy of the found route
        all_routes.append(current_route.copy())
        print(f"ROUTE FOUND: {' -> '.join(current_route)}")
    
    else:
        # Explore all unvisited neighbors (cycle prevention)
        for neighbor in range(MAX):
            if matrix[node_index][neighbor] == 1 and not visited[neighbor]:
                # Recursive call to neighbor
                dfs_recursive(neighbor)
    
    # Unmark node and remove from current route
    visited[node_index] = False
    current_route.pop()


# MOST OPTIMAL ROUTE EVALUATION
def find_optimal_route():
    """
    Evaluates all discovered routes to find the most optimal one
    the most optimal is the shortest route (minimum number of nodes visited to reach the end node)
    """
    if not all_routes:
        return None, None
    
    # Find route with minimum number of nodes
    optimal_route = None
    optimal_length = float('inf') #we begin with the largest possible value so that any route will be shorter that 'inifinity'
    
    for route in all_routes:
        route_length = len(route)  # Number of nodes in the route
        
        if route_length < optimal_length:
            optimal_length = route_length
            optimal_route = route
    
    # Cost = number of edges (nodes - 1)
    cost = optimal_length - 1 if optimal_route else 0
    
    return optimal_route, cost


def find_all_optimal_routes():
    """
    Finds all routes with the shortest length (if there are more than one optimal route)
    """
    if not all_routes:
        return []
    
    # Find minimum length
    min_length = min(len(route) for route in all_routes)
    
    # Filter all routes with that length
    optimal_routes = [route for route in all_routes if len(route) == min_length]
    
    return optimal_routes


# DISPLAY FUNCTIONS
def get_node_name(index):
    """Gets the node name from its index"""
    for name, idx in map_node.items():
        if idx == index:
            return name
    return f"Node_{index}"


def display_results():
    """
    Displays all results and triggers "Unable to reach end node" if blocked
    """
    print("\nROUTE ANALYSIS RESULTS\n")
    
    if not all_routes:
        print("\nError, unable to reach the end node")        
        return
    
    # Display all routes found
    print(f"\nFound {len(all_routes)} possible routes:\n")
    
    route_number = 1
    for route in all_routes:
        route_as_string = ' -> '.join(route)
        number_of_nodes = len(route)
        print(f"Route {route_number}: {route_as_string} (Length: {number_of_nodes} nodes)")
        route_number = route_number + 1 
    
    # Find and display the optimal route
    optimal_route, cost = find_optimal_route()
    
    if optimal_route:
        print("\nMOST OPTIMAL ROUTE (shortest):\n")
        print(f"Route: {' -> '.join(optimal_route)}")
        print(f"Nodes: {len(optimal_route)}")
        print(f"Edges: {cost}")
        
        # Show if there are multiple optimal routes
        all_optimal = find_all_optimal_routes()
        if len(all_optimal) > 1:
            print(f"\nThere are {len(all_optimal)} routes with the same optimal length:")
            for i, route in enumerate(all_optimal, 1):
                if route != optimal_route:
                    print(f"\tOptimal route {i}: {' -> '.join(route)}")


# CYCLE DETECTION
def has_cycle(node, visited_temp, recursion_stack):
    """
    Recursive function to detect cycles in the graph
    """
    visited_temp[node] = True
    recursion_stack[node] = True #tracks which nodes are in the current path
    
    for neighbor in range(MAX):
        if matrix[node][neighbor] == 1:
            if not visited_temp[neighbor]:
                if has_cycle(neighbor, visited_temp, recursion_stack):
                    return True
            elif recursion_stack[neighbor]: #This means we found a back edge or CYCLE
                return True

    #No cycle found from this node
    recursion_stack[node] = False 
    return False


def detect_cycles():
    """
    Detects if the graph has cycles 
    """
    visited_temp = [False for _ in range(MAX)] #any node has been visited yet
    recursion_stack = [False for _ in range(MAX)]
    
    for i in range(count_nodes):
        if not visited_temp[i]:
            if has_cycle(i, visited_temp, recursion_stack):
                return True
    
    return False #we didn't find any cycle in the graph


if __name__ == "__main__":
    print("")