#!/usr/bin/env python3

import unittest
from enum import Enum

from textnode import (
    TextNode,
    ValidTextTypes,
    split_nodes_delimiter,
    text_node_to_html_node
    )

class TestTextNode(unittest.TestCase):

    def setUp(self):
        self.base_node = TextNode("This is a text node", "bold")
        self.inline_bold = TextNode("foo bar **This is a text node** foo bar")

    def test_eq(self):
        node = self.base_node
        node2 = node
        self.assertEqual(node, node2)

    def test_type_exceptions(self):
        with self.assertRaises(TypeError):
            node = self.base_node
            node.text_type = 5
            print(node)
            node.text_type = ['regular', 'bold']
            print(node)

    def test_blank_type(self):
        self.assertEqual(
            self.inline_bold,
            TextNode("foo bar **This is a text node** foo bar", "text")
        )

    def test_url_exceptions(self):
        node = self.base_node
        with self.assertRaises(ValueError):
            node.url = "foo bar"
            print(node)
            node.url = "foo.bar"
            print(node)

    def test_node_conversion(self):
        pass

    def test_node_split(self):
        pass


if __name__ == "__main__":
    unittest.main()
