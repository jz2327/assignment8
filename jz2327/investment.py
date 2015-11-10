import numpy as np 
import exception_user
from exception_user import invalid_list_bound, invalid_list_value, invalid_trial_numbers

class investment_options():
	'''class created to read input from users and check if the input is valid. Assign the input to attributes.'''

	def __init__(self, positions_input, num_trials):
		positions = positions_input
		if positions[0] != '[' or positions[-1] != ']':   #check the input string has the right format of being a list.
			raise invalid_list_bound()
		else:
			positions_modified = positions[1:-1]
			positions_list = positions_modified.split(',')
			try:
				for position in range(len(positions_list)):
					positions_list[position] = int(positions_list[position])   #check if the elements in the list can be converted to integers.
			except:
				raise invalid_list_value()
		self.positions = np.array(positions_list)

		try: 
			int(num_trials)
		except:
			raise invalid_trial_numbers()   #check if the input of trial numbers can be converted to integers.
		self.num_trials = int(num_trials)
		self.position_value = 1000 / self.positions