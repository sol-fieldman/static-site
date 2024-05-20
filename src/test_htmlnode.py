#!/usr/bin/env python3

import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(None,None,None,{"foo":"bar","fizz":"buzz"})
        self.assertIsInstance(node.props_to_html(),str)
