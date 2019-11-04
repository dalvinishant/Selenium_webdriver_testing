from selenium import webdriver
import unittest
import HtmlTestRunner

class Test_class(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(r"D:\Softwares\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search(self):
        url = "http://google.com"
        print("Opening url : ", url)
        q = "Iglorious Empire by Sashi Tharoor"
        self.driver.get(url)
        self.driver.find_element_by_name("q").send_keys(q)
        print("Firing Query : ",q)
        self.driver.find_element_by_name("btnK").click()
        print("Query Fired Successfully")
        print("Result Loaded Sucessfully")

    def test_search1(self):
        url = "http://google.com"
        print("Opening url : ", url)
        q = "abcd"
        self.driver.get(url)
        self.driver.find_element_by_name("q").send_keys(q)
        print("Firing Query : ",q)
        self.driver.find_element_by_name("btnK1").click()
        print("Query Fired Successfully")
        print("Result Loaded Sucessfully")
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=("B:/practical-react/src/Testing_Results")))