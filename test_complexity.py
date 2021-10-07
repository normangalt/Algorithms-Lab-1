"Tests sorting algorithms."

import matplotlib.pyplot as plt
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from shellsort import shellsort
from generate_experiments import generate_test_arrays

XSCALE = [index for index in range(7, 15)]
ALGORITHMS = [selection_sort, insertion_sort, merge_sort, shellsort]

plt.style.use(['seaborn-darkgrid'])

def run_experiment(index: int = 0, toggle: bool = False):
	"""
	Runs an experiment.

	Args:
		index (int, optional): Index value of the experiment. Defaults to 0.
		toggle (bool, optional): whether to show the created graphs. Defaults to False.
	"""	
	global ALGORITHMS

	tests = generate_test_arrays()

	time_graph_space, operations_graph_space = config_spaces()
	time_graph_space.set_facecolor('tab:gray')
	operations_graph_space.set_facecolor('tab:gray')

	graph(tests, time_graph_space, operations_graph_space, toggle, index)

def config_spaces():
	"""
	Creates the axes spaces for the plotting.

	Returns:
		(Axe, Axe): axes for the plotting.
	"""
	_, (time_graph_space, operations_graph_space) = \
	plt.subplots(1, 2, figsize=(10, 5))

	time_graph_space.set_xlabel('Input size (power of 2)')
	operations_graph_space.set_xlabel('Input size (power of 2)')

	return time_graph_space, operations_graph_space

def graph(tests, time_graph_space, operations_graph_space, toggle = False, index = 0):
	"""
	Graphs the experiments.

	Args:
		tests (list): functions for input generation.
		time_graph_space (Object): axe for the time measure results.
		operations_graph_space (Object): axe for the number of operations count.
		toggle (bool, optional): whether to show the created graphs. Defaults to False.
		index (int): index value of the experiment.
	"""
	test = tests[index]
	index_color = 0
	for algorithm in ALGORITHMS:
		xscale, experiment_result_time, experiment_result_comparisons = algorithm_test_experiment(algorithm, test, index)

		plot_results_experiment(xscale, experiment_result_time, True, time_graph_space, index_color)
		plot_results_experiment(xscale, experiment_result_comparisons, False, operations_graph_space, index_color)
		index_color += 1

	time_graph_space.legend(['Selection sort', 'Insertion sort', 'Mergesort', 'Shellsort'], loc = 2)
	operations_graph_space.legend(['Selection sort', 'Insertion sort', 'Mergesort', 'Shellsort'], loc = 2)

	if toggle:
		plt.show()

	plt.savefig('Experiment__'+str(index)+'__.png')

def test_algorithm_case(algorithm, test_array):
	"""
	Tests the given algorithm on a given array.

	Args:
		algorithm ([Object]): algorithm to test.
		test_array ([list]): the lists to test on.

	Returns:
		list: a tuple with time and number of comparison operations.
	"""
	return [el for el in algorithm(test_array)]

def plot_results_experiment(xscale, experiment_results, option, graph_space, index):
	"""
	Plots the given data on the axe.

	Args:
		experiment_results ([list]): data to plot.
		option ([bool]): which case of the test is performed.
		graph_space ([Object]): an axe to plot on.
	"""
	ls=('dashed','dotted','solid','dashed')
	colors = ('blue', 'red', 'yellow', 'magenta')

	graph_space.plot(xscale,
					 experiment_results,
					 lw=3*(0.88**(2 - index)),
					 linestyle = ls[index],
					 alpha = 0.9**(index+2),
					 color = colors[index])

	if option:
		graph_space.set_ylabel('Time')

	else:
		graph_space.set_ylabel('Comparison operations')

def algorithm_test_experiment(algorithm: object = sorted, test: object = [], index: int = 0):
	"""
	Tests an algorithm on a given test.

	Args:
		algorithm (object, optional): An algorithm to test. Defaults to sorted.
		test (object, optional): function to use to generate test input. Defaults to [].
		index (int, optional): index number of the test. Defaults to 0.

	Returns:
		(list, list): a list with results of time and number of
of comparison operations used in the test.
	"""
	experiment_result_time = []
	experiment_result_comparisons = []
	size_powers = list(range(7, 15))
	sizes = [2**i for i in size_powers]

	for size in sizes:
		if index == 2:
			test_array = test(size, True) 	# generate an input array
											# according to the experiment number
		else:
			test_array = test(size)

		time, size_result_comparison = test_algorithm_case(algorithm, test_array)

		experiment_result_time.append(time)
		experiment_result_comparisons.append(size_result_comparison)

	return size_powers, experiment_result_time, experiment_result_comparisons

if __name__ == '__main__':
	for index in range(4):
		run_experiment(index = index, toggle = True)
