# EVOLVE-BLOCK-START
"""Constructor-based Coxeter radical of dimension k >= 2"""
import numpy as np

# Our individual import
##########################
import networkx as nx
import matplotlib as plt
import scipy as sp
import copy
##########################


def construct_graph():
    """
    Construct a specific simple connected graph such that the corresponding Coxeter group has a radical
    of dimension k>=2, that attempts to minimizes the sum of edges and vertices.
    Returns:
        Tuple of (G, num_v, num_e, sum)
        G: nx.Graph object
        num_v: integer
        num_e: integer
        sum: Sum of num_v + num_e
    """ 
    N = 13
    verts = [i+1 for i in range(N)]
    G = nx.Graph()

    # Add vertices
    for i in range(N): G.add_node(i+1)

    # Add edges
    for combi in combinations(verts,2):

      # Create initial rooted tree with 3 leafs 2,3,4
      if combi[0]==1 and combi[1] in [2,3,4]:
        G.add_edge(combi[0],combi[1])
      
      # Create square at leaf 2
      if combi[0]==2 and combi[1] in [5,6]: G.add_edge(combi[0],combi[1])
      if combi[0] in [5,6] and combi[1]==7:
        G.add_edge(combi[0],combi[1])
      
      # Create square at leaf 3
      if combi[0]==3 and combi[1] in [8,9]: G.add_edge(combi[0],combi[1])
      if combi[0] in [8,9] and combi[1]==10:
        G.add_edge(combi[0],combi[1])
      
      # Create square at leaf 4
      if combi[0]==4 and combi[1] in [11,12]: G.add_edge(combi[0],combi[1])
      if combi[0] in [11,12] and combi[1]==13:
        G.add_edge(combi[0],combi[1])

      # Compute sum of vertices and edges
      sum = G.number_of_nodes() + G.number_of_edges()

    return G, G.number_of_nodes(), G.number_of_edges(), sum

# EVOLVE-BLOCK-END


# This part remains fixed (not evolved)
def run_graph():                                                                                      #------> changed
    """Run the graph constructor"""
    G, num_v, num_e, sum = construct_graph()
    return G, num_v, num_e, sum


if __name__ == "__main__":                                                                            #------> changed
    G, num_v, num_e, sum = run_graph()
    print(f"Sum of num_v and num_e: {sum}")


    # Uncomment to visualize:
    #nx.draw(G)
