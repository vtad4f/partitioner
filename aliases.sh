#!/bin/bash

function clean { git clean -dfqX ; }
function reload { git fetch ; git checkout -B master origin/master ; }
function x { git update-index --chmod=+x $1 ; }

