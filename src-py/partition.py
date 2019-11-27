

import argparse
import random
import re
import sys


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
      self.pending_v = set()
      
   def AddVertex(self, vertices):
      """
         BRIEF  If no vertices have been added yet, pick a random one
                Else pick a random adjacent vertex
      """
      if not vertices:
         return None
         
      if not self.vertices:
         i = random.randint(0, len(vertices) - 1)
         v_index = list(vertices.keys())[i]
         
         v = vertices.pop(v_index)
         self.vertices.append(v)
         return v
         
      while self.pending_v:
         sys.stdout.flush()
         i = random.randint(0, len(self.pending_v) - 1)
         v_index = list(self.pending_v)[i]
         self.pending_v.remove(v_index)
         
         if v_index in vertices:
            
            v = vertices.pop(v_index)
            self.vertices.append(v)
            return v
            
   def AddEdges(self, edges, vertex):
      """
         BRIEF  Take every edge that contains the vertex
      """
      for i in reversed(range(len(edges))):
         if vertex.index in edges[i].vertices:
            e = edges.pop(i)
            self.edges.append(e)
            self.pending_v.update(e.vertices)
      self.pending_v.discard(vertex.index)
      
   def __repr__(self):
      """
         BRIEF  Conversion to a string
      """
      return "# t 1\n{0}\n{1}".format('\n'.join(map(str,self.vertices)), '\n'.join(map(str, self.edges)))
      
      
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
      
   vertices = dict([(v.index, v) for v in map(Vertex, Regex.VERTICES.findall(content))])
   edges = list(map(Edge, Regex.EDGES.findall(content)))
   
   partitions = [Graph()] * args.n
   while vertices:
      
      for graph in partitions:
         v = graph.AddVertex(vertices)
         if v:
            graph.AddEdges(edges, v)
            
   for graph in partitions:
      print(graph)
      
      