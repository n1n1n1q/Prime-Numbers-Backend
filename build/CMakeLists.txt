cmake_minimum_required(VERSION 3.4...3.18)
project(sieve)

find_package(pybind11 REQUIRED)
pybind11_add_module(sieve sieve.cpp)

target_compile_options(sieve PRIVATE 
    $<$<CONFIG:Debug>:-g>
    $<$<CONFIG:Release>:-O3>
)
