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

	fig, ax = plt.subplots()

	plt.title('Plot showing the locations of the positions of the obstacles')
	plt.xlabel('X coordinate')
	plt.ylabel('Y coordinate')

	plt.xlim(-3,3)
	plt.ylim(-3,3)

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

	plt.scatter(x_list, y_list, color='red')
	plt.grid()
	plt.show()
	print counter

if __name__ == '__main__':
	plotObstacles()