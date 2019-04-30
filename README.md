# Counting Obstacles in a scene using Swarm Robots
Directed Research for Spring 2019 - Collective perception for robot swarm in presence of faulty or byzantine robots. 

## Files and Usage ##

* `argos/obstacle_avoidance_environment.argos` is the XML environment file that creates the environment with
	- Arena Size  6 x 6
	- 6 obstacles - Cylinders
	- 8 Khepera IV robots

* The repository uses Makefile system for execution
* Run the command `make run` from the root directory of this repository to open up the ARGoS simulation environment with the Buzz editor
* Load the `buzz/counting_obstacle_avoidance.bzz` file as the main script for Argos
* Hit the execute button to run the setup. Currently, the final result, list {probability, x_coordinate, y_coordinate} elements representing the obstacles, is written to the file `results/store_data.txt`

* Visualize these obstacles determined by the swarm using `make plot` that opens up a Python matplotlib window showing the plot.

* `/results` folder also has a couple of comparison snapshots between the actual simulation environment and the one obtained from the swarm.

### Note: ###

* Edit the header file paths for includes in the `buzz/counting_obstacle_avoidance.bzz` file appropriately
* Delete the contents of the storage file `results/store_data.txt` before each run else information gets appended over multiple runs 
