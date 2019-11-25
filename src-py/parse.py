

import re
import sys


class Regex:
   SUBGRAPH = re.compile(r':[^:]+', re.MULTILINE)
   VERTICES = re.compile(r'v ([0-9]+) ([0-9]+)', re.MULTILINE)
   EDGES    = re.compile(r'e ([0-9]+) ([0-9]+) ([0-9]+)', re.MULTILINE)
   
   
class Edge(object):
   """
      BRIEF  An undirected edge
   """
   
   def __init__(self, labels):
      """
         BRIEF  Constructor

         PARAM labels  should be (vertex1 label, vertex2 label, edge label)
      """
      self.vertices = sorted(components[:2])
      self.label = labels[2]
      
   def __repr__(self):
      """
         BRIEF  Conversion to a string
      """
      return "{0}-{2}-{1}".format(*self.vertices, self.label)
      
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
      
      
class SubGraph(object):
   """
      BRIEF  A collection of vertices and edges
   """
   
   def __init__(self, text):
      """
         BRIEF  Constructor
                Parse string to get vertices and edges
      """
      vertices = dict(Regex.VERTICES.findall(text))
      self.vertices = sorted(vertices.values()) # labels only
      
      edges = [(vertices[v1], vertices[v2], label) for (v1, v2, label) in Regex.EDGES.findall(text)]
      self.edges = sorted(map(Edge, edges))
      
   def __repr__(self):
      """
         BRIEF  Conversion to a string
      """
      return "{0} {1}".format(str(self.vertices), str(self.edges))
      
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
      
      
if __name__ == '__main__':
   """
      BRIEF  Main execution
   """
   subgraphs = set()
   
   for path in sys.argv[1:]:
      with open(path, 'r') as f:
         subgraphs |= frozenset(map(SubGraph, Regex.SUBGRAPH.findall(f.read())))
         
   for s in sorted(subgraphs):
      print(s)
      
      