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
   time "${@:2}" > output.txt 2>&1
   popd > /dev/null 2>&1
}

function gen      { _Run src-py python gen.py $@ ; }
function gen.less { less src-py/random_graph ; }

function fsm      { _Run fsm ./gSpan-64 -f ../src-py/random_graph $@ ; }
function fsm.less { less fsm/output.txt ; }
