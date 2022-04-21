import unittest  # THE TEST MODULE !!!!!!!!!!!
from FunctionModule3 import get_formatted_name

class NameTestCase(unittest.TestCase):  # IT IS NECESSARY IT SAYS PYTHON HOW TO TEST !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def test_first_last_name(self):
        formatted_name = get_formatted_name('ege','selvi')
        self.assertEqual(formatted_name, 'Ege Selvi')  # CHECK WHETHER FUNCTION MATCHES WITH INPUT !!!
                                                        # COMPARE THE RESULTS !!!
    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name(
            'ege','selvi',middle = 'mercan'
        )
        self.assertEqual(formatted_name,'Ege Mercan Selvi')
unittest.main()



