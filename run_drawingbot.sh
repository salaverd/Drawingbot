#!/bin/bash

colcon build --packages-select drawingbot

source install/setup.bash

ros2 run drawingbot coords
