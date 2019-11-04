#!/bin/bash

function clean { git clean -dfqX ; }
function x { git update-index --chmod=+x $1 ; }

function reload
{
   git fetch
   git branch -m local
   git checkout -b master origin/master
   git branch -d local
}

function run.fsm
{
   pushd fsm > /dev/null 2>&1
   time ./gSpan-64 gIndex/dataset > output.txt 2>&1
   popd > /dev/null 2>&1
}

