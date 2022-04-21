import unittest
from ClassModule import Anonymous_Survey

class TestAnonymousSurvey(unittest.TestCase):  # NECESSARY !!! unittest.TestCase !!!
    def setUp(self):                            # PYTHON RUNS SETUP FIRST BEFORE EACH METHOD STARTING WITH TEST !!!!!!!
        question = "What lang did you first learn: "
        self.my_survey = Anonymous_Survey(question)
        self.responses = ['English','French','German']
    def test_store_single_response(self):
        self.my_survey.store_responses(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)
    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_responses(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)  # WE DONT NEED TWO SELF FOR THIS CODE !!!!!!!!!!!!!!!!!!
unittest.main()

