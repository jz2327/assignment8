import unittest
import numpy as np
from unittest import TestCase
import investment
from investment import investment_options
import investment_operating
import exception_user
from exception_user import invalid_list_bound, invalid_list_value, invalid_trial_numbers

class assignment8_test(TestCase):
	'''test the investment_options class'''

	def test_investment_options_isvalid(self):
		'''test if the class has an expected return when input is in right format'''
		
		investment_test = investment_options('[1, 10, 100, 1000]', '10000')
		self.assertTrue(np.array_equal(investment_test.positions, np.array([1, 10, 100, 1000])))
		self.assertTrue(investment_test.num_trials, 10000)

	def test_investment_options_invalid_list_bound(self):
		'''test if the class raises error when input string cannot be converted to a list'''

		self.assertRaises(invalid_list_bound, lambda: investment_options('[1, 10, 100, 1000', '10000'))

	def test_investment_options_invalid_list_value(self):
		'''test if the class raises error when the list has invalid elements'''

		self.assertRaises(invalid_list_value, lambda: investment_options('[1, 10, 100, invalid]', '10000'))

	def test_investment_options_isvalid_trial_numbers(self):
		'''test if the class raises error when the input trial numbers cannot be conveted to integer'''

		self.assertRaises(invalid_trial_numbers, lambda: investment_options('[1, 10, 100, 1000]', 'invalid'))

if __name__ == '__main__':
	unittest.main()

