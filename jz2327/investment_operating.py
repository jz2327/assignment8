import numpy as np
import matplotlib.pyplot as plt 

def one_time_investment(position_value):
	'''define a function to compute the return of one investment'''

	probability = np.random.randint(1,101)   #generate a random number with uniform distribution in [1, 100]
	if probability <= 49:   #the probability of investment with no return
		one_day_return = 0
	else:   #the probability of investment with double return 
		one_day_return = 2*position_value
	return one_day_return

def one_day_investment(positions, position_value):
	'''define a function to compute the return of investment in one day using function one_time_investment'''

	cumu_ret = 0
	for i in range(positions):
		cumu_ret += one_time_investment(position_value)
	daily_ret = float(cumu_ret)/1000 - 1   #return the daily return 
	return daily_ret

def num_trials_investment(positions, position_value, num_trials):
	'''define a function to iterate the return of investment in one day for num_trials times and compute the average return'''

	daily_ret = []
	for i in range(1, num_trials+1):
		daily_ret.append(one_day_investment(positions, position_value))
	return daily_ret

def plot_investment(positions, position_value, num_trials):
	'''define a function to plot the return in function num_trial_investment and save the image to a pdf file'''

	daily_ret = num_trials_investment(positions, position_value, num_trials)
	plt.figure()
	plt.hist(daily_ret, 100, range = [-1,1])
	plt.xlabel('Daily return')
	plt.title('histogram with positions: {}'.format(str(positions)))
	plt.savefig('histogram_{}_pos.pdf'.format(str(positions).zfill(4)))   #name the new file as required