# Copyright 2019 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Demo for spawn_entity.

Launches Gazebo and spawns a model
"""
import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    world_file_name = 'gazebo_ros_state_demo.world'
    pkg_dir = get_package_share_directory('testrosgazebo')
    world_path = os.path.join(pkg_dir, 'worlds', world_file_name)
    
    gzros_pkg_dir = get_package_share_directory('gazebo_ros')
    gzros_path = os.path.join(gzros_pkg_dir, 'launch')

    world_declare_arg = DeclareLaunchArgument(
                        'world', default_value=world_path,
                        description='Specify world file name'
                        )

    verbose_arg = DeclareLaunchArgument(
                    'verbose', default_value='true',
                    description='Set "true" to increase messages written to terminal.'
                    )


    gazebo_launch = IncludeLaunchDescription(
                    PythonLaunchDescriptionSource([gzros_path, '/gazebo.launch.py']),
                    )

    return LaunchDescription([
        world_declare_arg,
        verbose_arg,
        gazebo_launch,
    ])
