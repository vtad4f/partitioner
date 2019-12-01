

import gen
import parse
import partition
import subprocess
import sys


class Path:
   REPO_DIR        = 'D:/git/cs6304/partitioner'
   GRAMI_DIR       = REPO_DIR + '/GraMi'
   GRAMI_SCRIPT    = GRAMI_DIR + '/grami.sh'
   GRAMI_DATADIR   = GRAMI_DIR + '/Datasets'
   
   GEN_GRAPH_NAME  = 'random_graph.lg'
   GEN_GRAPH       = GRAMI_DATADIR + '/' + GEN_GRAPH_NAME
   
   
def GraMi(graph_fname, support):
   """
      BRIEF  
   """
   args = [
      'java', '-cp', './GRAMI_UNDIRECTED_SUBGRAPHS/bin', 'Dijkstra.main',
      'freq={0}'.format(support), 'filename={0}'.format(graph_fname),
      'datasetFolder=./Datasets/', 'distance=1', 'type=0',
      'mlabels=false', 'maxLabelAppearance=-1', 'approximate=1', 'approxConst=0'
   ]
   process = subprocess.Popen(args, stdout=subprocess.PIPE, cwd=Path.GRAMI_DIR)
   out, _ = process.communicate()
   return out.decode('utf-8')
   
   
if __name__ == '__main__':
   """
      BRIEF  Main execution
   """
   n_vertices   = 100
   n_edges      = 500
   support      = 4
   n_partitions = 3
   
   gen.Main(Path.GEN_GRAPH, n_vertices, n_edges)
   
   original = parse.SubGraphs(GraMi(Path.GEN_GRAPH_NAME, support))
   partitioned = set()
   
   n = 0
   while len(partitioned) < len(original):
      n += 1
      
      for fname in partition.Main(Path.GEN_GRAPH, n_partitions):
         partitioned |= parse.SubGraphs(GraMi(fname, support))
         
      print('{0}/{1}'.format(len(partitioned), len(original)))
      sys.stdout.flush()
      
   print('{0} iterations'.format(n))
   
   impossible = partitioned - original
   if impossible:
      for subgraph in sorted(impossible):
         print(subgraph)
         
   sys.stdout.flush()
   
   