

import argparse
import random
import re


class Regex:
   VERTICES = re.compile(r'v ([0-9]+) ([0-9]+)', re.MULTILINE)
   EDGES    = re.compile(r'e ([0-9]+) ([0-9]+) ([0-9]+)', re.MULTILINE)
   
   
class Vertex(object):
   """
      BRIEF  This object represents a vertex in a graph
   """
   
   def __init__(self, components):
      """
         BRIEF  Constructor

         PARAM components  should be (vertex index, vertex label)
      """
      self.index = components[0]
      self.label = components[1]
      
   def __repr__(self):
      """
         BRIEF  Conversion to a string
      """
      return "v {0} {1}".format(self.index, self.label)
      
   def __lt__(self, other):
      """
         BRIEF  Less than operator
      """
      return str(self) < str(other)
      
   def __eq__(self, other):
      """
         BRIEF  Equality than operator
      """
      return str(self) == str(other)
      
   def __hash__(self):
      """
         BRIEF  Necessary to store edges in a set or map
      """
      return hash(str(self))
      
      
class Edge(object):
   """
      BRIEF  This object represents an edge in a graph
   """
   
   def __init__(self, components):
      """
         BRIEF  Constructor

         PARAM components  should be (vertex1 index, vertex2 index, edge label)
      """
      self.vertices = sorted(components[:2])
      self.label = components[2]
      
   def __repr__(self):
      """
         BRIEF  Conversion to a string
      """
      return "e {0} {1} {2}".format(*self.vertices, self.label)
      
   def __lt__(self, other):
      """
         BRIEF  Less than operator
      """
      return str(self) < str(other)
      
   def __eq__(self, other):
      """
         BRIEF  Equality than operator
      """
      return str(self) == str(other)
      
   def __hash__(self):
      """
         BRIEF  Necessary to store edges in a set or map
      """
      return hash(str(self))
      
      
class Graph(object):
   """
      BRIEF  A container for vertices and edges
   """
   
   def __init__(self):
      """
         BRIEF  Constructor
      """
      self.vertices = []
      self.edges = []
      
   def AddVertex(self, vertices):
      """
         BRIEF  
      """
      if self.vertices:
         pass
      else:
         pass
         
   def __repr__(self):
      """
         BRIEF  Conversion to a string
      """
      return "# t 1\n{0}\n{1}".format('\n'.join(self.vertices), '\n'.join(self.edges))
      
      
if __name__ == '__main__':
   """
      BRIEF  Main execution
   """
   parser = argparse.ArgumentParser()
   parser.add_argument('input_fpath')
   parser.add_argument('output_dirpath')
   parser.add_argument('n', type=int)
   args = parser.parse_args()
   
   with open(args.input_fpath,'r') as f:
      content = f.read()
      
   vertices = map(Vertex, Regex.VERTICES.findall(content))
   edges = map(Edge, Regex.EDGES.findall(content))
   
   partitions = [Graph()] * args.n
   # while vertices:
      
      # for graph in partitions:
         # if not graph.AddVertex(vertices):
            # break
            
            