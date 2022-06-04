#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from testing.sum import sum_two

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum_two(1, 2), 3)
        self.assertEqual(sum_two(1, 3), 4)



if __name__ == '__main__':
    unittest.main()
