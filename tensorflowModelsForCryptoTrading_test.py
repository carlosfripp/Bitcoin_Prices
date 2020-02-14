# Libraries
import unittest

# Local module
from tensorflowModelsForCryptotrading import *

# TODO: Complete unittests

class VanillaNeuralNetwork_test(unittest.TestCase):
	def setUp(self):
		self.nn = VanillaNeuralNetwork()

	def tearDown(self):
		pass

	def test_assertWeightInit(self):
		pass
		# self.assertEquals()

if __name__ == "__main__":
	unittest.main()
	
