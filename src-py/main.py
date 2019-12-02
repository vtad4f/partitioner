

import gen
import parse
import partition
import argparse
import subprocess
import sys
import time


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
   
   # Parse args
   import argparse
   parser = argparse.ArgumentParser()
   parser.add_argument('n_vertices',     type=int)
   parser.add_argument('percent_edges',  type=float, help=' of max n edges')
   parser.add_argument('support',        type=int)
   parser.add_argument('n_partitions',   type=int)
   parser.add_argument('--repartitions', type=int, default=24, help='max attempts', metavar='N')
   args = parser.parse_args()
   
   # Percent is applied to the max number of edges
   min_n_edges = args.n_vertices
   max_n_edges = args.n_vertices * (args.n_vertices - 1) / 2
   n_edges = int(args.percent_edges * max_n_edges)
   
   # Validate args
   assert(0.0 < args.percent_edges <= 1.0)
   assert(min_n_edges <= n_edges <= max_n_edges)
   assert(args.support >= 2)
   assert(args.n_partitions >= 2)
   
   # Generate random graph
   gen.Main(Path.GEN_GRAPH, args.n_vertices, n_edges)
   print('finished generating random graph!')
   sys.stdout.flush()
   
   # Parse with GraMi
   start = time.monotonic()
   original = parse.SubGraphs(GraMi(Path.GEN_GRAPH_NAME, args.support))
   print('{0} total subraphs'.format(len(original))) 
   print("{:0.2f} seconds for the analysis".format(time.monotonic() - start))
   sys.stdout.flush()
   
   # Skip partitioning if there are no subgraphs to be found
   if len(original) > 0:
      partitioned = set()
      last_len = len(partitioned)
      start = time.monotonic()
      
      # Repartition until we find all the subgraphs
      for i in range(args.repartitions + 1): 
         if original and len(partitioned) >= len(original):
            break
            
         # Generate partitions
         partitions = partition.Main(Path.GEN_GRAPH, args.n_partitions)
         print('-', end='')
         sys.stdout.flush()
         
         # Run GraMi against each partition
         for fname in partitions:
            partitioned |= parse.SubGraphs(GraMi(fname, args.support))
            print('.', end='')
            sys.stdout.flush()
            
         # Print status
         if len(partitioned) > last_len:
            last_len = len(partitioned)
            print('{0}/{1}'.format(len(partitioned), len(original)), end='')
            sys.stdout.flush()
         
      # Output results
      print('\n{0} iterations'.format(i + 1))
      print("{:0.2f} seconds for the analysis".format(time.monotonic() - start))
      
      impossible = partitioned - original
      if impossible:
         for subgraph in sorted(impossible):
            print(subgraph)
            
      sys.stdout.flush()
   
   