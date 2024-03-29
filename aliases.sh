#!/bin/bash

function clean  { git clean -dfqX ; }
function x      { git update-index --chmod=+x $1 ; }
function reload { git fetch ; git rebase origin/master ; source aliases.sh ; }

function frun   { sbatch batch.sub ; } # run job on mst forge
function fls    { squeue -u vtad4f ; } # list running jobs
function fkill  { scancel $1       ; } # kill a running job

function _Run
{
   pushd "$1" > /dev/null 2>&1
   time "${@:2}"
   popd > /dev/null 2>&1
}


GEN_GRAPH_NAME=random_graph.lg
GEN_GRAPH_PATH=GraMi/Datasets/$GEN_GRAPH_NAME
GRAMI_OUTPUT=GraMi/output.txt


function grami      { _Run GraMi ./grami.sh -f $GEN_GRAPH_NAME -s 2 -t 0 -p 0 > $GRAMI_OUTPUT ; }
function grami.less { less $GRAMI_OUTPUT ; }

function gen        { _Run src-py py gen.py ../$GEN_GRAPH_PATH $@ ; }
function gen.less   { less $GEN_GRAPH_PATH ; }

function parse      { _Run src-py py parse.py ../$GRAMI_OUTPUT $@ ; }

function partition  { _Run src-py py partition.py ../$GEN_GRAPH_PATH $@ ; }

function main       { _Run src-py py main.py $@ ; }

function setup
{
   if [[ ! -d GraMi ]]; then
      git clone https://github.com/vtad4f/GraMi.git GraMi
      cd GraMi
      ./build.sh
      cd -
   fi
}