cmake_minimum_required(VERSION 2.8.12)
project(counting_obstacle_avoidance)

find_package(Buzz REQUIRED)
#include_directories(${BUZZ_C_INCLUDE_DIR})
#target_link_libraries(... ${BUZZ_LIBRARY})
include(UseBuzz)
set(BUZZ_BZZ_INCLUDE_DIR ${BUZZ_BZZ_INCLUDE_DIR} ${CMAKE_SOURCE_DIR}/..)
buzz_make(counting_obstacle_avoidance.bzz INCLUDES helpers.bzz)