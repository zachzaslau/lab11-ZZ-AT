# https://github.com/zachzaslau/lab11-ZZ-AT/tree/main
# Partner 1: Zach Zaslau
# Partner 2: Anthony Toscano

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEquals(add(3,3), 9)
        self.assertEquals(add(-1,2), 1)
        self.assertEquals(add(0,0), 0)

    def test_subtract(self): # 3 assertions
        self.assertEquals(sub(0,0), 0)
        self.assertEquals(sub(1, -1), 2)
        self.assertEquals(sub(5, 10), -5)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEquals( mul(2, 2), 4 )
        self.assertEquals( mul( -2, 3 ), -6 )
        self.assertEquals( mul( 100, 6 ), 600 )

    def test_divide(self): # 3 assertions
        self.assertEquals( div(1, 1), 1)
        self.assertEquals( div( 1, 3 ), 3 )
        self.assertEquals( div( 2, 10 ), 5 )
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code
        self.assertRaises(ZeroDivisionError, div(0,5))

    def test_logarithm(self): # 3 assertions
    #     fill in code
        self.assertEquals(log(10,1),0)
        self.assertEquals(log(10,100), 2)
        self.assertEquals(log(10,1000), 3)

    def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
        self.assertRaise(ValueError, log(-1,10))
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        self.assertRaises( ValueError, log( 0, 10) )

    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    def test_hypotenuse(self): # 3 assertions
        self.assertEquals( hypotenuse( 3, 4 ), 5 )
        self.assertEquals( hypotenuse( 7, 24 ), 25 )
        self.assertEquals( hypotenuse( 6, 8 ), 10 )

    def test_sqrt(self): # 3 assertions
        self.assertRaises( ValueError, square_root(-1) )
        self.assertEquals( square_root( 1 ), 1 )
        self.assertEquals( square_root( 4 ), 2 )
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()