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
        subcount = [sub for sub in list if "Amazon" in sub]
        self.assertEqual(len(subcount), 18)
    
    def test_longest_answer(self):
        list = convert_to_list("qa/dataset/Answers.txt")
        self.assertEqual(len(max(list, key=len)), 1456)

    def test_number_topics(self):
        list = convert_to_list("qa/dataset/Topics.txt")
        self.assertEqual(len(set(list)), 130)
        
    def test_procfile(self):
        file = open("Procfile").read()
        self.asserTrue(file.split("--port=",1)[1] == "$PORT")
