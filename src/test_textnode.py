#!/usr/bin/env python3

import unittest

from textnode import *
from htmlnode import *

class TestTextNode(unittest.TestCase):

    def setUp(self):
        self.base_node = TextNode("This is a text node", ValidTextTypes.bold)
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
            node.text_type = [ValidTextTypes.text,
                              ValidTextTypes.bold]
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
        self.assertEqual(
            text_node_to_html_node(self.base_node),
            LeafNode("b","This is a text node")
        )
        self.assertEqual(
            text_node_to_html_node(self.inline_bold),
            LeafNode(None, "foo bar **This is a text node** foo bar")
        )

    def test_node_split(self):
        self.assertEqual(
            split_nodes_delimiter([self.inline_bold],"**",ValidTextTypes.bold),
            [
                TextNode("foo bar "),
                self.base_node,
                TextNode(" foo bar")
            ]
        )


if __name__ == "__main__":
    unittest.main()
