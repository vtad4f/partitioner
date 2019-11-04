#!/bin/bash

function clean { git clean -dfqX ; }
function x { git update-index --chmod=+x $1 ; }

function reload
{
   git fetch
   git rebase origin/master
}


function _Run
{
   pushd "$1" > /dev/null 2>&1
   time "${@:2}" > output.txt 2>&1
   popd > /dev/null 2>&1
}

function run.gen { _Run src-py python gen.py $1 $2 ; }
function run.fsm { _Run fsm ./gSpan-64 ../src-py/random_graph ; }

