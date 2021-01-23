cmake_minimum_required(VERSION 2.8)

project(ThreeSqaures2-2)
add_executable(${PROJECT_NAME} "main.cpp" "midaco.c")
find_package(PythonLibs 2.7)
target_include_directories(ThreeSqaures2-2 PRIVATE ${PYTHON_INCLUDE_DIRS})
target_link_libraries(ThreeSqaures2-2 ${PYTHON_LIBRARIES})
