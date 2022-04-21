import unittest
from ClassModule import Anonymous_Survey

class TestAnonymousSurvey(unittest.TestCase):  # NECESSARY !!! unittest.TestCase !!!

    def test_store_single_response(self):
        question = "What lang did you first learn: "
        my_survey = Anonymous_Survey(question)
        my_survey.store_responses('English')
        self.assertIn('English',my_survey.responses)
    def test_store_three_responses(self):
        question = "What lang did you first learn: "
        my_survey = Anonymous_Survey(question)
        responses = ['English','French','German']
        for response in responses:
            my_survey.store_responses(response)
        for response in responses:
            self.assertIn(response,my_survey.responses)
unittest.main()


