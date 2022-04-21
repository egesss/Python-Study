import unittest  # THE TEST MODULE !!!!!!!!!!!
from FunctionModule3 import get_formatted_name

class NameTestCase(unittest.TestCase):  # IT IS NECESSARY IT SAYS PYTHON HOW TO TEST !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def test_first_last_name(self):
        formatted_name = get_formatted_name('ege','selvi')
        self.assertEqual(formatted_name, 'Ege Selvi')  # CHECK WHETHER FUNCTION MATCHES WITH INPUT !!!
                                                        # COMPARE THE RESULTS !!!

unittest.main()

#.
#----------------------------------------------------------------------
#Ran 1 test in 0.000s

#OK

# OUTPUT SAYS FUNCTION WORKS !!!!!

#----------------------------------------------------------------------
#Ran 1 test in 0.000s

#FAILED (errors=1)

# OUTPUT SAYS FUNCTION DOESN'T WORKS !!!!!

# WHEN OUR TEST IS FAILED, WE DON'T CHANGE THE TEST, CHANGE THE MODULE !!!