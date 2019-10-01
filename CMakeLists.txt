

cmake_minimum_required(VERSION 3.0.0)

set (SRC   
   main.cpp
)

set (proj partitioner)
project(${proj})
add_executable(${proj} ${SRC})
include_directories(${proj} . )
set_target_properties(${proj} PROPERTIES COMPILE_OPTIONS "-Wall" "--std=c++11" "-g")

