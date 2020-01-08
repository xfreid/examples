# http://derekmolloy.ie/hello-world-introductions-to-cmake/
# As your project grows, it is likely that you will organize it into sub-directories. Makefiles become more verbose when there are sub-directories present, in fact, it is usual practice to place an individual Makefile in each sub-directory. These Makefiles are then individually invoked by the Makefile in the parent directory.
# CMake can be very useful in this situation. In this example, a project with a typical directory structure is used. 
# molloyd@beaglebone:~/exploringBB/extras/cmake/student$ tree
# .
# |-- CMakeLists.txt
# |-- build
# |-- include
# |   \-- Student.h
# \-- src
#     |-- Student.cpp
#     \-- mainapp.cpp
# 3 directories, 4 files

cmake_minimum_required(VERSION 2.8.9)
project(directory_test)


# Bring the headers, such as Student.h into the project
# The include_directories() function is used to bring the header files into the build environment.
include_directories(include)

# Can manually add the sources using the set command as follows:
# The set(SOURCES ...) function can be used to set a variable (SOURCES) that contains the name values of all of the source files (.cpp) in the project. However, because each source file must be added manually the next line is used in its place, and this line is commented out.
#set(SOURCES src/mainapp.cpp src/Student.cpp)

# However, the file(GLOB...) allows for wildcard additions:
# The file() command is used to add the source files to the project. GLOB (or GLOB_RECURSE) is used to create a list of all of the files that meet the globbing expression (i.e., src/*.cpp) and add them to a variable SOURCES.
file(GLOB SOURCES "src/*.cpp")

# The add_executable() function uses the SOURCES variable, rather than an explicit reference to each source file, in order to build the testStudent executable program.
add_executable(testStudent ${SOURCES})

# For this example, I wish to place all of the build files in the build directory, which is achieved very simply by calling the cmake program from within the build directory, as follows:
#  molloyd@beaglebone:~/exploringBB/extras/cmake/student$ cd build
#  molloyd@beaglebone:~/exploringBB/extras/cmake/student/build$ cmake ..


