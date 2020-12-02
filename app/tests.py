from app import is_alive_host
import requests
import unittest
from unittest.mock import patch


class Tests(unittest.TestCase):

    def mock_response(self, status):
        mock_resp = unittest.mock.Mock()
        mock_resp.status_code = status
        return mock_resp

    @patch('requests.head')
    def test_alive_host_100(self, mock_resp):
        mock_resp.return_value = self.mock_response(100)
        self.assertTrue(is_alive_host("google.com"))

    @patch('requests.head')
    def test_alive_host_200(self, mock_resp):
        mock_resp.return_value = self.mock_response(200)
        self.assertTrue(is_alive_host("google.com"))

    @patch('requests.head')
    def test_alive_host_300(self, mock_resp):
        mock_resp.return_value = self.mock_response(300)
        self.assertTrue(is_alive_host("google.com"))

    @patch('requests.head')
    def test_down_host_403(self, mock_resp):
        mock_resp.return_value = self.mock_response(403)
        self.assertFalse(is_alive_host("google.com"))

    @patch('requests.head')
    def test_down_host_404(self, mock_resp):
        mock_resp.return_value = self.mock_response(404)
        self.assertFalse(is_alive_host("google.com"))

    @patch('requests.head')
    def test_down_host_500(self, mock_resp):
        mock_resp.return_value = self.mock_response(500)
        self.assertFalse(is_alive_host("google.com"))

    @patch('requests.head')
    def test_down_host_502(self, mock_resp):
        mock_resp.return_value = self.mock_response(502)
        self.assertFalse(is_alive_host("google.com"))


if __name__ == "__main__":
    unittest.main()