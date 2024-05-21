#!/usr/bin/env python3

import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold", "https://foo.bar")
        node2 = TextNode("This is a text node", "bold", "https://foo.bar")
        self.assertEqual(node, node2)

    def test_style(self):
        with self.assertRaises(TypeError):
            node = TextNode("This is a text node", None, "foo.bar")
            print(node)

            node.text_type = 5
            print(node)

            node.text_type = ['regular', 'bold']
            print(node)

    def test_url(self):
        with self.assertRaises(TypeError):
            print(TextNode("This is a text node", "bold", None))
        with self.assertRaises(ValueError):
            print(TextNode("This is a text node", "bold", "foo bar"))
            print(TextNode("This is a text node", "bold", "foo.bar"))


if __name__ == "__main__":
    unittest.main()
