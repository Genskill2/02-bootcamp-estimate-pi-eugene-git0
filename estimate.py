import math
import unittest
import random

def wallis(n):
	pi_cal=1
	for i in range (1,n):
		pi_cal = pi_cal*(4 * (i ** 2)) / ((4 * (i ** 2)) - 1)
	pi_cal =  2 * pi_cal
	return pi_cal
	
def monte_carlo(n):
	x=0
	y=0
	inn=0
	for i in range (1,n):
		x = random.random()**2
		y = random.random()**2
		if(math.sqrt(x+y))<1.00:
			inn = inn + 1
	pi_cal = (float(inn)/n)*4
	return pi_cal
	
class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()
