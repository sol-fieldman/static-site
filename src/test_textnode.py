#!/usr/bin/env python3

import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold", "https://foo.bar")
        node2 = TextNode("This is a text node", "bold", "https://foo.bar")
        self.assertEqual(node, node2)

    def test_blank_style(self):
        node = TextNode("This is a text node", None, "foo.bar")
        node2 = node
        self.assertEqual(node, node2)

    def test_blank_url(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = node
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
