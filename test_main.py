import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np
import unittest
import main

class UnitTests(unittest.TestCase) :
    def test_mean_exists(self) :
       self.assertTrue( "mean" in globals(), "The variable mean was not defined in your code" )
       
    def test_mean_correct(self) : 
       mymean = sum(x) / len(x)
       self.assertTrue( np.abs(mymean-mean)<1e-7, "The variable mean does not have the correct value" )
