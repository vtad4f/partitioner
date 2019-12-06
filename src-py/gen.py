

import random


def Main(fpath, n_vertices, n_edges, v_range=10, e_range=10):
   """
      BRIEF  Main execution (all but cmd line parsing)
   """
   
   # Create file with single graph
   with open(fpath, 'w') as f:
      f.write('# t 1\n')
      
      # Add vertices
      vertices = range(n_vertices)
      for v in vertices:
         f.write('v {0} {1}\n'.format(v, random.choice(range(v_range))))
         
      # Add edges
      edges = set()
      for e in range(n_edges):
         
         success = False
         while not success:
            
            this_vertex  = e if e < len(vertices) else random.choice(vertices)
            other_vertex = random.choice(vertices)
            
            # No cyclic graphs
            if this_vertex != other_vertex:
               
               # Don't write the same edge twice
               directed = [this_vertex, other_vertex]
               undirected = frozenset(directed)
               if not undirected in edges:
                  edges.add(undirected)
                  
                  success = True
                  
                  random.shuffle(directed)
                  f.write('e {0} {1} {2}\n'.format(directed[0], directed[1], random.choice(range(e_range))))
                  
                  
if __name__ == '__main__':
   """
      BRIEF  Main execution (including cmd line parsing)
   """
   import argparse
   parser = argparse.ArgumentParser()
   parser.add_argument('path')
   parser.add_argument('v', type=int)
   parser.add_argument('e', type=int)
   args = parser.parse_args()
   Main(args.path, args.v, args.e)
   