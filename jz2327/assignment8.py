import numpy as np 
import matplotlib.pyplot as plt
import sys
import investment
import investment_operating
from investment import investment_options
import exception_user
from exception_user import invalid_list_bound, invalid_list_value, invalid_trial_numbers

'''
Main program for assignment 8.
Also see readme.txt for instructions.
'''


try:
	while True:
		positions = raw_input('Input a list of the number of shares: ')
		num_trials = raw_input('Input how many times to ramdomly repeat the test: ')
		try:	
			investment_list = investment_options(positions, num_trials)
			with open('results.txt', 'w') as f:   #save the results to result.txt
				for i in range(len(investment_list.positions)):
					daily_ret = investment_operating.num_trials_investment(investment_list.positions[i], investment_list.position_value[i], investment_list.num_trials)
					investment_operating.plot_investment(investment_list.positions[i], investment_list.position_value[i], investment_list.num_trials)
					print 'the mean of the daily return is: ' + str(np.mean(daily_ret))
					print 'the stadard deviation of the daily return is: ' + str(np.std(daily_ret))
					f.write('\n' + 'Positions: ' + str(investment_list.positions[i]) + ' Position values: '+ str(investment_list.position_value[i]) + ' trial numbers: ' + str(investment_list.num_trials))
					f.write('\n' + 'the mean of the daily return is: ' + str(np.mean(daily_ret)))
					f.write('\n' + 'the stadard deviation of the daily return is: ' + str(np.std(daily_ret)))
		except invalid_list_bound:
			print 'Invalid list bound!'
		except invalid_list_value:
			print 'Invalid list value!'
		except invalid_trial_numbers:
			print 'Invalid trial number!'
		loop_continue = raw_input('continue for another loop? \n (Enter no/n to exit the program, enter other words to start a new loop)')
		if str.lower(loop_continue) == 'no' or str.lower(loop_continue) == 'n':   #enter no/n(upper is allowed) to exit the program
			sys.exit()

except (KeyboardInterrupt, EOFError):
	print 'Terminate abnormally'

