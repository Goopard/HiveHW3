"""
This is a unittest test case for the whole module user_agent_parser.
"""

import unittest
import sys

from io import StringIO
from user_agents import parse


class Mocker:
    """
    This class is used as a context manager to mock the sys.stdin and sys.stdout with some StringIO objects.
    """
    def __init__(self, contents):
        """Here we initialize the value of the mocked stdin.

        :param contents: Text that will be written in the mocked stdin.
        :type contents: str.
        """
        self.contents = contents

    def __enter__(self):
        """
        This method is called on the entrance of the context manager. Here we mock stdin and stdout with StringIO
        objects.
        """
        self.old_stdin = sys.stdin
        sys.stdin = StringIO(self.contents)
        self.old_stdout = sys.stdout
        sys.stdout = StringIO()

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        This method is called on the exit of the context manager, here we return sys.stdin and sys.stdout to their
        natural state.
        """
        sys.stdin = self.old_stdin
        sys.stdout = self.old_stdout


class Tests(unittest.TestCase):
    def setUp(self):
        """
        Here we read the values of the input files to use them later in tests.
        """
        with open('test_inputs\\test_1', 'r') as file:
            self.first_input = file.read()
        with open('test_inputs\\test_2', 'r') as file:
            self.second_input = file.read()

    def test_1(self):
        with Mocker(self.first_input), open('..\\user_agent_parser.py', 'r') as source:
            code = source.read()
            exec(code)
            results = sys.stdout.getvalue()
            self.assertEqual(results, '218	Other	Windows	Firefox\n322	Other	Windows	Chrome'
                                      '\n289	Other	Windows	IE\n255	Other	Windows	Chrome\n')

    def test_2(self):
        with Mocker(self.second_input), open('..\\user_agent_parser.py', 'r') as source:
            code = source.read()
            exec(code)
            results = sys.stdout.getvalue()
            self.assertEqual(results, '333	Other	Windows	Chrome\n222	Other	Windows	IE'
                                      '\n111	Other	Windows	IE\n444	Other	Windows	IE\n')


if __name__ == '__main__':
    unittest.main()
