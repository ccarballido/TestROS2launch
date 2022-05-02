# testrosgazebo

Package to test how to use launch files in ROS2 and the launch files provided by gazebo_ros package
There are 3 launch files, all open gazebo with gazebo_ros_state_demo.world

## test1.launch.py
File to launch without building the package.
Go to testrosgazebo/launch folder and launch test1 
```
ros2 launch test1.launch.py
```

## test2.launch.py
File to launch building the package, not using gazebo_ros packages
Build with colcon, source and launch
```
. install/setup.bash
ros2 launch testrosgazebo test2.launch.py
```

## test3.launch.py
File to launch building the package, using gazebo_ros packages
Build with colcon, source and launch
```
. install/setup.bash
ros2 launch testrosgazebo test3.launch.py
```
