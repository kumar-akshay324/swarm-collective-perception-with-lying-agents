# Counting Obstacles in a scene using Swarm Robots
Directed Research for Spring 2019 - Collective perception for robot swarm in presence of faulty or byzantine robots. 

##Files and Usaee##

* `argos/obstacle_avoidance_environment.argos` is the XML environment file that creates the environment with
	- Arena Size  6 x 6
	- 6 obstacles - Cylinders
	- 8 Khepera IV robots

* Run the command `argos3 -c argos/obstacle_avoidance_environment.argos` from the root directory of this repository
* Load the `buzz/counting_obstacle_avoidance.bzz` file as the main script for Argos

**Note: Edit the header file paths for includes in the `buzz/counting_obstacle_avoidance.bzz` file appropriately** 