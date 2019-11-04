

cmake_minimum_required(VERSION 3.0.0)

set (SRC
   main.cpp
   src-cpp/Client.cpp
   src-cpp/Client.h
   src-cpp/Graph.cpp
   src-cpp/Graph.h
)

set (proj partitioner)
project(${proj})
add_executable(${proj} ${SRC})
include_directories(${proj} . )
set_target_properties(${proj} PROPERTIES COMPILE_OPTIONS "-Wall" "--std=c++11" "-g")

