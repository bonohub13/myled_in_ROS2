#!/usr/bin/env bash

curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add -
sh -c 'echo "deb [arch=amd64,arm64] http://packages.ros.org/ros2/ubuntu `lsb_release -cs` main" > /etc/apt/sources.list.d/ros2-latest.list'

apt update
apt install -y ros-dashing-ros-base

echo "source /opt/ros/dashing/setup.bash >> ~/.bashrc"
source ~/.bashrc

apt install -y \
	python3-argcomplete \
	python3-colcon-common-extensions \
	python3-rosdep

rosdep init
rosdep update

echo "Finished ros2 installation sequence!"
