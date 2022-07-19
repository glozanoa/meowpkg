#!/usr/bin/env python3

import unittest

from meowpkg.example import add_one

class TestExample(unittest.TestCase):
    def test_add_one(self):
        self.assertEqual(2, add_one(1))
