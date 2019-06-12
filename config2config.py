import networkx as nx
import itertools as it

G = nx.Graph()
c=it.permutations(range(8),4) #8 possile cells , 4 knights, W for white and B for black knight
for i in c:
    config = ['_'] * 8
    config[i[0]] = 'W'
    config[i[1]] = 'W'
    config[i[2]] = 'B'
    config[i[3]] = 'B'
    G.add_node("".join(config))  
#print(G.nodes) #list of configurations

#the knights can move from ith position to k_move[i] th positions 
K_moves=[[4, 6],[5, 7],[3, 6],[2, 7],[0, 5],[1, 4],[0, 2],[1, 3]]

for node in G.nodes():
    config = [i for i in node] 
    for i in range(8):
        if config[i] != "_":
            for p in K_moves[i]: 
                if config[p] != "_":
                    continue
                new_config = list(config) 
                new_config[i] = "_"
                new_config[p] = config[i] 
                if not G.has_edge("".join(config), "".join(new_config)):
                    G.add_edge("".join(config), "".join(new_config))                 
                   
#nx.draw(G,node_size=1,line_width=.1,pos=nx.spring_layout(G))
print(nx.number_of_nodes(G))
print(nx.number_of_edges(G))
print(nx.number_connected_components(G)) # one connected component contains all configurations where along this cycle two white knights are followed by two black knights, while the other connected components consists of all configurations where the white and black knights are interchanged. 

situ_1=input(('ENTER THE STARTING CONFIGURATION (Use the format "W_W__B_B") :'))
situ_2=input(('ENTER THE FINAL CONFIGURATION (Use the format "W_W__B_B") :'))

try:
    if situ_1 in nx.node_connected_component(G, situ_2):
      print(" -> ".join(nx.shortest_path(G, situ_1, situ_2))) #gives us the shortest path if possible 
      c=nx.shortest_path(G, situ_1, situ_2)
      print("Number of moves=",len(c)-1)
except: 
    print("Not Possible")
