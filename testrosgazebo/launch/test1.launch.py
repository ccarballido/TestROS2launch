# Copyright 2021 cesar_carballido
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
Launches Gazebo and gazebo_ros_state_demo.world
"""

from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():

    gazebo = ExecuteProcess(
            cmd=['gazebo', '--verbose', '../worlds/gazebo_ros_state_demo.world', '-s', 'libgazebo_ros_init.so'],
            output='screen')


    return LaunchDescription([
        gazebo,
    ])