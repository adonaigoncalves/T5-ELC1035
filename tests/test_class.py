import unittest
from qa.app import app
from qa.parsedata import convert_to_list

class TestAskMe(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
    
    def tearDown(self):
        pass
        
    def test_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_num_docs(self):
        list = convert_to_list("qa/dataset/Answers.txt")
        self.assertEqual(len(list), 2609)

    def test_first_answer(self):
        list = convert_to_list("qa/dataset/Answers.txt")
        self.assertTrue(list.index("Ten")==0)

    def test_count_amazon(self):
        list = convert_to_list("qa/dataset/Answers.txt")
        substrings = [sub for sub in list if "Amazon" in sub]
        self.assertEqual(substrings.count("Amazon"), 46)
        
