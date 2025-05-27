#!/usr/bin/env python3
"""Generic utilities for github org client.
""" 

import unittest
from utils import access_nested_map
from parameterized import expand


class TestAccessNestedMap(unittest.TestCase):

    @expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)