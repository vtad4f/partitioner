#!/bin/bash

function clean { git clean -dfqX ; }
function x { git update-index --chmod=+x $1 ; }

function reload
{
   git fetch
   git rebase origin/master
   source aliases.sh
}

function _Run
{
   pushd "$1" > /dev/null 2>&1
   time "${@:2}"
   popd > /dev/null 2>&1
}

function gen      { _Run src-py python gen.py $@ ; }
function gen.less { less src-py/random_graph ; }

function grami      { _Run GraMi ./grami random_graph.lg -s 2 -t 0 -p 0 > GraMi/output.txt ; }
function grami.less { less GraMi/output.txt ; }
