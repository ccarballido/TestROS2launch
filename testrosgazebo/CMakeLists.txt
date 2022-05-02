cmake_minimum_required(VERSION 3.5)
project(testrosgazebo)

find_package(ament_cmake REQUIRED)
find_package(gazebo_ros REQUIRED)


install(DIRECTORY  launch  DESTINATION share/${PROJECT_NAME}/)
install(DIRECTORY  worlds  DESTINATION share/${PROJECT_NAME}/)

ament_package()
