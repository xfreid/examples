# The first line sets the minimum version of CMake for this project, which is major version 2, minor version 8, and patch version 9 in this example. 
# The second line is the project() command that sets the project name.
# The third line is the add_executable() command, which requests that an executable is to be built using the HelloWorld.cpp source file. The first argument to the add_executable() function is the name of the executable to be built, and the second argument is the source file from which to build the executable.

cmake_minimum_required(VERSION 2.8.9)
project (hello)
add_executable(hello HelloWorld.cpp)

# execute the cmake command and pass it the directory that contains the source code and the CMakeLists.txt file in this case '.' refers to the current directory
