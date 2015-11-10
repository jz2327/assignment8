class invalid_list_bound(Exception):
	'''Raise error of invalid list.'''

	def __str__(self):
		return 'invalid list: invalid format of list!'

class invalid_list_value(Exception):
	'''Raise error of invalid value in the list.'''

	def __str__(self):
		return 'invalid list: invalid value!'

class invalid_trial_numbers(Exception):
	'''Raise error of invalid trial numbers.'''

	def __str__(self):
		return 'invalid number: not an integer!'