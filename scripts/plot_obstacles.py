#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import os
import matplotlib.cm as cm

# PATH = "/media/akshay/anything_Else/WorcesterPolytechnicInstitute/SemIV/DirectedResearch/collective-perception-with-lying-agents/results"

PATH = os.getcwd()
FILE_NAME = "results/store_data.txt"

PROB_THRESHOLD = 0.5

def plotObstacles():
	final_file = os.path.join(PATH, FILE_NAME)
	counter = 0

	x_list = []
	y_list = []

	x_list_low = []
	y_list_low = []


	prob_list = []

	fig, (ax1, ax2) = plt.subplots(1,2)
	
	ax1.set_title('Plot showing the locations of the positions of the obstacles')
	ax1.set_xlabel('X coordinate')
	ax1.set_ylabel('Y coordinate')

	ax1.set_xlim(-3,3)
	ax1.set_ylim(-3,3)

	ax2.set_title('Common Probability values observed')
	ax2.set_ylabel('Probability')

	with open(final_file, "r") as coordinates_file:
		for line in coordinates_file:
			prob, x_coord, y_coord = line.split(" ")
			prob = float(prob)
			x_coord = float(x_coord)
			y_coord = float(y_coord)

			if (prob > PROB_THRESHOLD):
				counter += 1
				x_list.append(x_coord)
				y_list.append(y_coord)
				# print (x_coord, "   " ,type(x_coord))
				# print (y_coord, "   " ,type(y_coord))
			else:
				x_list_low.append(x_coord)
				y_list_low.append(y_coord)

			if prob not in prob_list:
				prob_list.append(prob)

	ax1.scatter(x_list, y_list, color='red', label="Obstacles with probability over the threshold")
	# ax1.Circle(((x_list, y_list), 0.05))
	ax1.scatter(x_list_low, y_list_low, color='blue', label="Obstacles with very low probability ")
	ax1.legend()
	ax1.grid()

	ax2.plot(prob_list)
	plt.show()
	print counter

if __name__ == '__main__':
	plotObstacles()