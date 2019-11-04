#!/bin/bash

function clean { git clean -dfqX ; }
function reload { git fetch ; git checkout -B master origin/master ; }
function x { git update-index --chmod=+x $1 ; }

function run.fsm
{
   pushd fsm > /dev/null 2>&1
   time ./gSpan-64 gIndex/dataset > output.txt 2>&1
   popd > /dev/null 2>&1
}

