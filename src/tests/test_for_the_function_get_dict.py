"""
This is a unittest test case for the function get_dict() from the module user_agent_parser.
"""

import unittest
from user_agent_parser import get_dict


class Tests(unittest.TestCase):
    def test_1(self):
        user_agent_line = 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)'
        self.assertEqual(get_dict(user_agent_line), {'Device': 'Other', 'OS': 'Windows', 'Browser': 'IE'})

    def test_2(self):
        user_agent_line = 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.31 (KHTML, like Gecko) ' \
                          'Chrome/26.0.1410.64 Safari/537.31'
        self.assertEqual(get_dict(user_agent_line), {'Device': 'Other', 'OS': 'Windows', 'Browser': 'Chrome'})

    def test_3(self):
        user_agent_line = 'Mozilla/5.0 (Windows NT 5.1; rv:24.0) Gecko/20100101 Firefox/24.0'
        self.assertEqual(get_dict(user_agent_line), {'Device': 'Other', 'OS': 'Windows', 'Browser': 'Firefox'})


if __name__ == '__main__':
    unittest.main()
