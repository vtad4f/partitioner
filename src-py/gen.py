

import argparse
import random


class Label:
   """
      BRIEF  
   """
   VERTEX = list(range(10))
   EDGE   = list(range(10))
   
   
if __name__ == '__main__':
   """
      BRIEF  Main execution
   """
   
   # Parse args
   parser = argparse.ArgumentParser()
   parser.add_argument('path')
   parser.add_argument('v')
   parser.add_argument('e')
   args = parser.parse_args()
   
   # Create file with single graph
   with open(args.path, 'w') as f:
      f.write('# t 1\n')
      
      # Add vertices
      vertices = range(int(args.v))
      for v in vertices:
         f.write('v {0} {1}\n'.format(v, random.choice(Label.VERTEX)))
         
      # Add edges
      edges = set()
      for e in range(int(args.e)):
         
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
                  f.write('e {0} {1} {2}\n'.format(directed[0], directed[1], random.choice(Label.EDGE)))
                  
                  