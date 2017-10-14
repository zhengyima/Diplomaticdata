cmake_minimum_required(VERSION 3.8)
project(gcc)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES main.cpp)
add_executable(gcc ${SOURCE_FILES})