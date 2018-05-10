# -*- coding: utf-8 -*-
import unittest

from mooquant_mootdx.api import get_quotes


class TestQuotes(unittest.TestCase):

    def test_get_quotes(self):
        data = get_quotes('600036')
        self.assertTrue(data is not None)

if __name__ == '__main__':
    unittest.main()
