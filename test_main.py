import unittest
import requests


class TestGHApi(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://localhost:5000/api"


    def test_users(self):
        base = f"{self.base_url}/users"
        response = requests.get(base)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("users" in response.json())
        self.assertTrue("next_page_link" in response.json()) 


    def test_get_user_details(self):
        username = "octocat"
        base = f"{self.base_url}/users/{username}/details"
        response = requests.get(base)
        self.assertEqual(response.status_code, 200)
    

    def test_get_user_repos(self):
        username = "octocat"
        base = f"{self.base_url}/users/{username}/repos"
        response = requests.get(base)
        self.assertEqual(response.status_code, 200)



if __name__ == "__main__":
    unittest.main()


""" para lograr que se ejecute el test, en la terminal de VSC ejecute este archivo: 
    "main.cpython-310.pyc"
    se abrira una ventana que ejecuta el servidor y de ahi ejecute esta ventana y corre el test"""
