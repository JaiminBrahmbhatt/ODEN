import warnings
warnings.filterwarnings("ignore")

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import sys, getopt

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('pdf', 'svg')
import matplotlib
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
from matplotlib.colors import LogNorm
import scipy
from scipy import special
from scipy.integrate import solve_ivp

#Import the Dictionary class
from Dictionary import Dictionary
D = Dictionary()
Dict = D.Dict

#Import the ODE solver class
from ODEsolver import ODEsolver

#Import the DiffEq class
from DiffEq import DiffEq

#Random seed initialization
seed = 1234
np.random.seed(seed)
tf.random.set_seed(seed)

#Custom plot fontsize
import os
os.environ['PATH'] = os.environ['PATH'] + ':/Library/TeX/texbin/'
from matplotlib import cm
from matplotlib import rc
plt.rcParams['axes.labelsize'] = 15                                                                                                     
plt.rcParams['legend.fontsize'] = 10                                                                                                     
plt.rcParams['xtick.labelsize'] = 10                                                                                                     
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['text.usetex'] = False
plt.rcParams['font.family'] = "serif"                                                                                                   
plt.rcParams['font.serif'] = "cm"

#--TODO
# 4096

if __name__ == "__main__":
	
	def exact_sol (x,a,b):
		m1 = (1 - np.sqrt(1 + 4 * (a + b)) ) / ( 2 * (a + b) )
		m2 = (1 + np.sqrt(1 + 4 * (a + b)) ) / ( 2 * (a + b) )
		c1 = (1 + np.exp(m2)) / (np.exp(m2) - np.exp(m1))
		c2 = (1 + np.exp(m1)) / (np.exp(m2) - np.exp(m1))

		exact = (c1 * np.exp(m1 * x) )- ( c2 * np.exp(m2 * x))

		return exact

	'''
	Variables for user input a, b, points, epochs
	'''
	# DEFAULT
	a = 1
	b = 1e-12
	points = 16
	epochs = 50000
	layers = 1
	neurons = 8
	dimens = [8]
	

	argv = sys.argv[1:]

	try:
		opts, args = getopt.getopt(argv,"ha:b:p:e:l:n:",["a=","b=", "points=", "epochs=","layers=","neurons="])
	except getopt.GetoptError:
		print('Experiment2.py -a <value_a> -b <value_b> -p <points> -e <epochs> -l <no.of_layers> -n <no.of_neurons>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
	 		print('Experiment2.py -a <value_a> -b <value_b> -p <points> -e <epochs> -l <no.of_layers> -n <no.of_neurons>')
	 		sys.exit()
		elif opt in ("-a", "--value_a"):
	 		a = float(arg)
		elif opt in ("-b", "--value_b"):
	 		b = float(arg)
		elif opt in ("-p", "--points"):
			points = int(arg)
		elif opt in ("-e", "--epochs"):
			epochs = int(arg)
		elif opt in ("-l", "--layers"):
			layers = int(arg)
		elif opt in ("-n", "--neurons"):
			neurons = int(arg)


	dimens = []
	for i in range(layers):
		dimens.append(neurons)
		i = i + 1

	order = 2
	diffeq = "experiment_2"

	x = np.linspace(0, 1, points, endpoint=True)[1:] 
	x0, y0 = 0, 1 
	dx0, dy0 = 1, 1 # 1,1 
	initial_condition = ((x0, y0), (dx0, dy0))
	architecture = dimens
	initializer = Dict["initializer"]["GlorotNormal"]
	activation = Dict["activation"]["sigmoid"]
	optimizer = Dict["optimizer"]["Adamax"]
	prediction_save = False
	weights_save = False

	#Plotting for epochs
	epochs = 50000
	solver = ODEsolver(order, diffeq, x, initial_condition, epochs, architecture, initializer, activation, optimizer, prediction_save, weights_save, a, b)
	history = solver.train()
	epoch, loss = solver.get_loss(history)
	x_predict = np.linspace(0, 1, points)
	y_predict = solver.predict(x_predict)


	plt.figure(1)
	plt.title(f'a = {a} points = {points} architecture = {dimens}')
	#plt.plot(x_exact, y_exact,color = "black", label = "Exact Solution")
	plt.plot(x_predict, y_predict, ".", color = "red", markersize = 6, label = "Neural Network Solution")
	plt.xlabel("$x$", fontsize = 15)
	plt.ylabel("$y(x)$", fontsize = 15)
	plt.xlim(min(x_predict), max(x_predict))
	plt.legend()
	plt.show()
	# a_1_points_16.png
	plt.savefig(f'OutputPlots/a_{a}_points_{points}.png')

	with open(f'OutputValues/a_{a}.txt', 'a') as f:
		line = f'a = {a}, b = {b}, points = {points}, architecture = {dimens} \n'
		f.write(line)

	