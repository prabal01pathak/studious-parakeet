#!/usr/bin/env python
# -*- coding: utf-8 -*-

from testing.sum import sum, call_seconds
import unittest

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(1, 2), 3)
        self.assertEqual(sum(1, 3), 4)



if __name__ == '__main__':
    unittest.main()

