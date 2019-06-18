import unittest
from qa.app import app
from qa.parsedata import convert_to_list
from selenium import webdriver

class TestAskMe(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()

    def test_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_num_docs(self):
        self.assertEqual(len(convert_to_list("qa/dataset/Answers.txt")), 2609)

    def test_title(self):
        self.browser.get('https://frozen-shelf-61168.herokuapp.com/')
        self.assertIn('Question Answering', self.browser.title)
