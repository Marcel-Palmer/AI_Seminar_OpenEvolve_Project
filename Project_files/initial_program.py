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
    
    E =[(1, 2), 
         (1, 3),
         (1, 4),
         (2, 9),
         (2, 10),
         (3, 5),
         (3, 6),
         (4, 7),
         (4, 8),
         (5, 12),
         (6,12),
         (7, 13),
         (8,13),
         (9, 11),
         (10,11)]
    

    G = nx.Graph(E)

    sum = G.number_of_nodes() + G.number_of_edges()
    
    return G, len(list(G)), G.number_of_edges(), sum

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